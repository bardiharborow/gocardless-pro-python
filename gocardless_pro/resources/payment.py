# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Payment(object):
    """A thin wrapper around a payment, providing easy access to its
    attributes.

    Example:
      payment = client.payments.get()
      payment.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def amount(self):
        return self.attributes.get('amount')
  

    @property
    def amount_refunded(self):
        return self.attributes.get('amount_refunded')
  

    @property
    def charge_date(self):
        return self.attributes.get('charge_date')
  

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def currency(self):
        return self.attributes.get('currency')
  

    @property
    def description(self):
        return self.attributes.get('description')
  

    @property
    def fx(self):
        return self.Fx(self.attributes.get('fx'))
  

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
    def reference(self):
        return self.attributes.get('reference')
  

    @property
    def retry_if_possible(self):
        return self.attributes.get('retry_if_possible')
  

    @property
    def status(self):
        return self.attributes.get('status')
  


  

  

  

  

  

  

  
    class Fx(object):
        """Wrapper for the response's 'fx' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def estimated_exchange_rate(self):
            return self.attributes.get('estimated_exchange_rate')
    
        @property
        def exchange_rate(self):
            return self.attributes.get('exchange_rate')
    
        @property
        def fx_amount(self):
            return self.attributes.get('fx_amount')
    
        @property
        def fx_currency(self):
            return self.attributes.get('fx_currency')
    
  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
        @property
        def instalment_schedule(self):
            return self.attributes.get('instalment_schedule')
    
        @property
        def mandate(self):
            return self.attributes.get('mandate')
    
        @property
        def payout(self):
            return self.attributes.get('payout')
    
        @property
        def subscription(self):
            return self.attributes.get('subscription')
    
  

  

  

  

  

