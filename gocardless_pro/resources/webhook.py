# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Webhook(object):
    """A thin wrapper around a webhook, providing easy access to its
    attributes.

    Example:
      webhook = client.webhooks.get()
      webhook.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def is_test(self):
        return self.attributes.get('is_test')
  

    @property
    def request_body(self):
        return self.attributes.get('request_body')
  

    @property
    def request_headers(self):
        return self.attributes.get('request_headers')
  

    @property
    def response_body(self):
        return self.attributes.get('response_body')
  

    @property
    def response_body_truncated(self):
        return self.attributes.get('response_body_truncated')
  

    @property
    def response_code(self):
        return self.attributes.get('response_code')
  

    @property
    def response_headers(self):
        return self.attributes.get('response_headers')
  

    @property
    def response_headers_content_truncated(self):
        return self.attributes.get('response_headers_content_truncated')
  

    @property
    def response_headers_count_truncated(self):
        return self.attributes.get('response_headers_count_truncated')
  

    @property
    def successful(self):
        return self.attributes.get('successful')
  

    @property
    def url(self):
        return self.attributes.get('url')
  


  

  

  

  

  

  

  

  

  

  

  

  

  

