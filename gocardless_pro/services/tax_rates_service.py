# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class TaxRatesService(base_service.BaseService):
    """Service class that provides access to the tax_rates
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.TaxRate
    RESOURCE_NAME = 'tax_rates'


    def list(self,params=None, headers=None):
        """List tax rates.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of all
        tax rates.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              TaxRate
        """
        path = '/tax_rates'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single tax rate.

        Retrieves the details of a tax rate.

        Args:
              identity (string): The unique identifier created by the jurisdiction, tax type and version
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of TaxRate instances
        """
        path = self._sub_url_params('/tax_rates/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  
