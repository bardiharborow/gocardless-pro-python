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
def test_creditors_create():
    fixture = helpers.load_fixture('creditors')['create']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.create(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.can_create_refunds, body.get('can_create_refunds'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.custom_payment_pages_enabled, body.get('custom_payment_pages_enabled'))
    assert_equal(response.fx_payout_currency, body.get('fx_payout_currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.logo_url, body.get('logo_url'))
    assert_equal(response.mandate_imports_enabled, body.get('mandate_imports_enabled'))
    assert_equal(response.merchant_responsible_for_notifications, body.get('merchant_responsible_for_notifications'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.scheme_identifiers, body.get('scheme_identifiers'))
    assert_equal(response.verification_status, body.get('verification_status'))
    assert_equal(response.links.default_aud_payout_account,
                 body.get('links')['default_aud_payout_account'])
    assert_equal(response.links.default_cad_payout_account,
                 body.get('links')['default_cad_payout_account'])
    assert_equal(response.links.default_dkk_payout_account,
                 body.get('links')['default_dkk_payout_account'])
    assert_equal(response.links.default_eur_payout_account,
                 body.get('links')['default_eur_payout_account'])
    assert_equal(response.links.default_gbp_payout_account,
                 body.get('links')['default_gbp_payout_account'])
    assert_equal(response.links.default_nzd_payout_account,
                 body.get('links')['default_nzd_payout_account'])
    assert_equal(response.links.default_sek_payout_account,
                 body.get('links')['default_sek_payout_account'])
    assert_equal(response.links.default_usd_payout_account,
                 body.get('links')['default_usd_payout_account'])

@responses.activate
def test_creditors_create_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('creditors')['create']
    helpers.stub_response(fixture)
    helpers.client.creditors.create(*fixture['url_params'])
    helpers.client.creditors.create(*fixture['url_params'])
    assert_not_equal(responses.calls[0].request.headers.get('Idempotency-Key'),
                     responses.calls[1].request.headers.get('Idempotency-Key'))

def test_timeout_creditors_create_idempotency_conflict():
    create_fixture = helpers.load_fixture('creditors')['create']
    get_fixture = helpers.load_fixture('creditors')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.creditors.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))

    assert_is_instance(response, resources.Creditor)

@responses.activate
def test_timeout_creditors_create_retries():
    fixture = helpers.load_fixture('creditors')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditors.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)

def test_502_creditors_create_retries():
    fixture = helpers.load_fixture('creditors')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditors.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)
  

@responses.activate
def test_creditors_list():
    fixture = helpers.load_fixture('creditors')['list']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.list(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Creditor)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.address_line1 for r in response.records],
                 [b.get('address_line1') for b in body])
    assert_equal([r.address_line2 for r in response.records],
                 [b.get('address_line2') for b in body])
    assert_equal([r.address_line3 for r in response.records],
                 [b.get('address_line3') for b in body])
    assert_equal([r.can_create_refunds for r in response.records],
                 [b.get('can_create_refunds') for b in body])
    assert_equal([r.city for r in response.records],
                 [b.get('city') for b in body])
    assert_equal([r.country_code for r in response.records],
                 [b.get('country_code') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.custom_payment_pages_enabled for r in response.records],
                 [b.get('custom_payment_pages_enabled') for b in body])
    assert_equal([r.fx_payout_currency for r in response.records],
                 [b.get('fx_payout_currency') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.logo_url for r in response.records],
                 [b.get('logo_url') for b in body])
    assert_equal([r.mandate_imports_enabled for r in response.records],
                 [b.get('mandate_imports_enabled') for b in body])
    assert_equal([r.merchant_responsible_for_notifications for r in response.records],
                 [b.get('merchant_responsible_for_notifications') for b in body])
    assert_equal([r.name for r in response.records],
                 [b.get('name') for b in body])
    assert_equal([r.postal_code for r in response.records],
                 [b.get('postal_code') for b in body])
    assert_equal([r.region for r in response.records],
                 [b.get('region') for b in body])
    assert_equal([r.scheme_identifiers for r in response.records],
                 [b.get('scheme_identifiers') for b in body])
    assert_equal([r.verification_status for r in response.records],
                 [b.get('verification_status') for b in body])

@responses.activate
def test_timeout_creditors_list_retries():
    fixture = helpers.load_fixture('creditors')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditors.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Creditor)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_creditors_list_retries():
    fixture = helpers.load_fixture('creditors')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditors.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Creditor)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_creditors_all():
    fixture = helpers.load_fixture('creditors')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.creditors.all())
    assert_equal(len(all_records), len(fixture['body']['creditors']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Creditor)
    
  

@responses.activate
def test_creditors_get():
    fixture = helpers.load_fixture('creditors')['get']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.get(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.can_create_refunds, body.get('can_create_refunds'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.custom_payment_pages_enabled, body.get('custom_payment_pages_enabled'))
    assert_equal(response.fx_payout_currency, body.get('fx_payout_currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.logo_url, body.get('logo_url'))
    assert_equal(response.mandate_imports_enabled, body.get('mandate_imports_enabled'))
    assert_equal(response.merchant_responsible_for_notifications, body.get('merchant_responsible_for_notifications'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.scheme_identifiers, body.get('scheme_identifiers'))
    assert_equal(response.verification_status, body.get('verification_status'))
    assert_equal(response.links.default_aud_payout_account,
                 body.get('links')['default_aud_payout_account'])
    assert_equal(response.links.default_cad_payout_account,
                 body.get('links')['default_cad_payout_account'])
    assert_equal(response.links.default_dkk_payout_account,
                 body.get('links')['default_dkk_payout_account'])
    assert_equal(response.links.default_eur_payout_account,
                 body.get('links')['default_eur_payout_account'])
    assert_equal(response.links.default_gbp_payout_account,
                 body.get('links')['default_gbp_payout_account'])
    assert_equal(response.links.default_nzd_payout_account,
                 body.get('links')['default_nzd_payout_account'])
    assert_equal(response.links.default_sek_payout_account,
                 body.get('links')['default_sek_payout_account'])
    assert_equal(response.links.default_usd_payout_account,
                 body.get('links')['default_usd_payout_account'])

@responses.activate
def test_timeout_creditors_get_retries():
    fixture = helpers.load_fixture('creditors')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditors.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)

def test_502_creditors_get_retries():
    fixture = helpers.load_fixture('creditors')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditors.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)
  

@responses.activate
def test_creditors_update():
    fixture = helpers.load_fixture('creditors')['update']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.update(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.can_create_refunds, body.get('can_create_refunds'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.custom_payment_pages_enabled, body.get('custom_payment_pages_enabled'))
    assert_equal(response.fx_payout_currency, body.get('fx_payout_currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.logo_url, body.get('logo_url'))
    assert_equal(response.mandate_imports_enabled, body.get('mandate_imports_enabled'))
    assert_equal(response.merchant_responsible_for_notifications, body.get('merchant_responsible_for_notifications'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.scheme_identifiers, body.get('scheme_identifiers'))
    assert_equal(response.verification_status, body.get('verification_status'))
    assert_equal(response.links.default_aud_payout_account,
                 body.get('links')['default_aud_payout_account'])
    assert_equal(response.links.default_cad_payout_account,
                 body.get('links')['default_cad_payout_account'])
    assert_equal(response.links.default_dkk_payout_account,
                 body.get('links')['default_dkk_payout_account'])
    assert_equal(response.links.default_eur_payout_account,
                 body.get('links')['default_eur_payout_account'])
    assert_equal(response.links.default_gbp_payout_account,
                 body.get('links')['default_gbp_payout_account'])
    assert_equal(response.links.default_nzd_payout_account,
                 body.get('links')['default_nzd_payout_account'])
    assert_equal(response.links.default_sek_payout_account,
                 body.get('links')['default_sek_payout_account'])
    assert_equal(response.links.default_usd_payout_account,
                 body.get('links')['default_usd_payout_account'])

@responses.activate
def test_timeout_creditors_update_retries():
    fixture = helpers.load_fixture('creditors')['update']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditors.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)

def test_502_creditors_update_retries():
    fixture = helpers.load_fixture('creditors')['update']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditors.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)
  
