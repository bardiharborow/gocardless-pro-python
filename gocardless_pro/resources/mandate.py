# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Mandate(object):
    """A thin wrapper around a mandate, providing easy access to its
    attributes.

    Example:
      mandate = client.mandates.get()
      mandate.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def consent_parameters(self):
        return self.ConsentParameters(self.attributes.get('consent_parameters'))
  

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def metadata(self):
        return self.attributes.get('metadata')
  

    @property
    def next_possible_charge_date(self):
        return self.attributes.get('next_possible_charge_date')
  

    @property
    def payments_require_approval(self):
        return self.attributes.get('payments_require_approval')
  

    @property
    def reference(self):
        return self.attributes.get('reference')
  

    @property
    def scheme(self):
        return self.attributes.get('scheme')
  

    @property
    def status(self):
        return self.attributes.get('status')
  


  
    class ConsentParameters(object):
        """Wrapper for the response's 'consent_parameters' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def end_date(self):
            return self.attributes.get('end_date')
    
        @property
        def max_amount_per_payment(self):
            return self.attributes.get('max_amount_per_payment')
    
        @property
        def periods(self):
            return self.attributes.get('periods')
    
        @property
        def start_date(self):
            return self.attributes.get('start_date')
    
  

  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def new_mandate(self):
            return self.attributes.get('new_mandate')
    
  

  

  

  

  

  

  

