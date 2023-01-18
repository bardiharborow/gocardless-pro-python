# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_scheme_identifiers_list():
    fixture = helpers.load_fixture('scheme_identifiers')['list']
    helpers.stub_response(fixture)
    response = helpers.client.scheme_identifiers.list(*fixture['url_params'])
    body = fixture['body']['scheme_identifiers']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.SchemeIdentifier)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.address_line1 for r in response.records],
                 [b.get('address_line1') for b in body])
    assert_equal([r.address_line2 for r in response.records],
                 [b.get('address_line2') for b in body])
    assert_equal([r.address_line3 for r in response.records],
                 [b.get('address_line3') for b in body])
    assert_equal([r.can_specify_mandate_reference for r in response.records],
                 [b.get('can_specify_mandate_reference') for b in body])
    assert_equal([r.city for r in response.records],
                 [b.get('city') for b in body])
    assert_equal([r.country_code for r in response.records],
                 [b.get('country_code') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response.records],
                 [b.get('currency') for b in body])
    assert_equal([r.email for r in response.records],
                 [b.get('email') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.minimum_advance_notice for r in response.records],
                 [b.get('minimum_advance_notice') for b in body])
    assert_equal([r.name for r in response.records],
                 [b.get('name') for b in body])
    assert_equal([r.phone_number for r in response.records],
                 [b.get('phone_number') for b in body])
    assert_equal([r.postal_code for r in response.records],
                 [b.get('postal_code') for b in body])
    assert_equal([r.reference for r in response.records],
                 [b.get('reference') for b in body])
    assert_equal([r.region for r in response.records],
                 [b.get('region') for b in body])
    assert_equal([r.scheme for r in response.records],
                 [b.get('scheme') for b in body])
    assert_equal([r.status for r in response.records],
                 [b.get('status') for b in body])

@responses.activate
def test_timeout_scheme_identifiers_list_retries():
    fixture = helpers.load_fixture('scheme_identifiers')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.scheme_identifiers.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['scheme_identifiers']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.SchemeIdentifier)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_scheme_identifiers_list_retries():
    fixture = helpers.load_fixture('scheme_identifiers')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.scheme_identifiers.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['scheme_identifiers']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.SchemeIdentifier)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_scheme_identifiers_all():
    fixture = helpers.load_fixture('scheme_identifiers')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.scheme_identifiers.all())
    assert_equal(len(all_records), len(fixture['body']['scheme_identifiers']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.SchemeIdentifier)
    
  

@responses.activate
def test_scheme_identifiers_get():
    fixture = helpers.load_fixture('scheme_identifiers')['get']
    helpers.stub_response(fixture)
    response = helpers.client.scheme_identifiers.get(*fixture['url_params'])
    body = fixture['body']['scheme_identifiers']

    assert_is_instance(response, resources.SchemeIdentifier)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.can_specify_mandate_reference, body.get('can_specify_mandate_reference'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.email, body.get('email'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.minimum_advance_notice, body.get('minimum_advance_notice'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.phone_number, body.get('phone_number'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_timeout_scheme_identifiers_get_retries():
    fixture = helpers.load_fixture('scheme_identifiers')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.scheme_identifiers.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['scheme_identifiers']

    assert_is_instance(response, resources.SchemeIdentifier)

def test_502_scheme_identifiers_get_retries():
    fixture = helpers.load_fixture('scheme_identifiers')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.scheme_identifiers.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['scheme_identifiers']

    assert_is_instance(response, resources.SchemeIdentifier)
  
