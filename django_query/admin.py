from django.contrib import admin
from django.contrib.admin.utils import lookup_spawns_duplicates
from django.core.checks import messages
from django.core.exceptions import FieldDoesNotExist, FieldError, ValidationError
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.utils.text import smart_split, unescape_string_literal


class QueryAdmin(admin.ModelAdmin):
    search_symbols = {
        ":[": "__in",
        ":": "__icontains",
        ">=": "__gte",
        "<=": "__lte",
        ">": "__gt",
        "<": "__lt",
        "=": "__iexact",
    }
    search_m2m_field = "__in"

    def get_search_results(self, request, queryset, search_term):
        """
        Return a tuple containing a queryset to implement the search
        and a boolean indicating if the results may contain duplicates.
        """

        matching = [s for s in self.search_symbols if s in search_term]

        if len(matching) == 0:
            return super().get_search_results(request, queryset, search_term)

        def construct_search(term):
            field, value = None, None

            # Looks for search_symbols and translates them to django's syntax
            for symbol, lookup in self.search_symbols.items():
                if term.find(symbol) > -1 and field is None:
                    field, value = term.split(symbol, 1)
                    field = f"{field.replace('.', '__')}{lookup}"

                    # If looking in an M2M field, use __in and remove the last square bracket
                    if lookup == self.search_m2m_field:
                        value = value.split("]")[0]

            # Clean the value
            if value.startswith(('"', "'")) and value[0] == value[-1]:
                value = unescape_string_literal(value)

            if value.startswith(" "):
                value = value[1:-1]

            return field, value

        may_have_duplicates = False

        if search_term:
            search_field, search_query = construct_search(search_term)

            try:
                or_queries = models.Q((search_field, search_query))
                queryset = queryset.filter(or_queries)
            except FieldError:
                self.message_user(
                    request, f"Invalid search term: {search_term}", level=messages.ERROR
                )
                return queryset, may_have_duplicates
            except ValidationError as e:
                self.message_user(request, e.messages[0], level=messages.ERROR)
                return queryset, may_have_duplicates

            may_have_duplicates |= lookup_spawns_duplicates(self.opts, search_field)

        return queryset, may_have_duplicates
