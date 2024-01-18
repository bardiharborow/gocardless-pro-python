# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class BankDetailsLookupsService(base_service.BaseService):
    """Service class that provides access to the bank_details_lookups
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.BankDetailsLookup
    RESOURCE_NAME = 'bank_details_lookups'


    def create(self,params=None, headers=None):
        """Perform a bank details lookup.

        Performs a bank details lookup. As part of the lookup, a modulus check
        and
        reachability check are performed.
        
        If your request returns an [error](#api-usage-errors) or the
        `available_debit_schemes`
        attribute is an empty array, you will not be able to collect payments
        from the
        specified bank account. GoCardless may be able to collect payments from
        an account
        even if no `bic` is returned.
        
        Bank account details may be supplied using [local
        details](#appendix-local-bank-details) or an IBAN.
        
        _ACH scheme_ For compliance reasons, an extra validation step is done
        using
        a third-party provider to make sure the customer's bank account can
        accept
        Direct Debit. If a bank account is discovered to be closed or invalid,
        the
        customer is requested to adjust the account number/routing number and
        succeed in this check to continue with the flow.
        
        _Note:_ Usage of this endpoint is monitored. If your organisation
        relies on GoCardless for
        modulus or reachability checking but not for payment collection, please
        get in touch.

        Args:
              params (dict, optional): Request body.

        Returns:
              BankDetailsLookup
        """
        path = '/bank_details_lookups'
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  
