from docusign_esign import AccountsApi
from .ds_client import DsClient

def get_idv_workflow(session):
    """Retrieve the workflow id"""
    api_client = DsClient.get_configured_instance(access_token=session["access_token"])

    workflow_details = AccountsApi(api_client)
    workflow_response = workflow_details.get_account_identity_verification(
        account_id=session["account_id"]
    )

    # Check that idv authentication is enabled
    if workflow_response.identity_verification:
        workflow_id = workflow_response.identity_verification[0].workflow_id
        return workflow_id

    return None

def is_sms_workflow(session):
    """Retrieve the workflow id"""
    api_client = DsClient.get_configured_instance(access_token=session["access_token"])

    workflow_details = AccountsApi(api_client)
    workflow_response = workflow_details.list_settings(
        account_id=session["account_id"]
    )

    # Check that sms authentication is enabled
    return workflow_response.allow_sms_delivery
