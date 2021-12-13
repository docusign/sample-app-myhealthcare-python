from datetime import date, datetime
from docusign_esign import (
    EnvelopesApi,
    EnvelopeDefinition,
    TemplateRole,
    RecipientPhoneNumber,
    RecipientAdditionalNotification,
    RecipientViewRequest,
    CarbonCopy,
    Tabs,
    Text,
    Email
)
from .ds_client import DsClient

class Envelope:

    @staticmethod
    def send(session, envelope_definition):
        """
        Sending an envelope
        """
        api_client = DsClient.get_configured_instance(
            access_token=session["access_token"]
        )
        envelopes_api = EnvelopesApi(api_client)
        envelope = envelopes_api.create_envelope(
            account_id=session["account_id"],
            envelope_definition=envelope_definition
        )
        return envelope.envelope_id

    @staticmethod
    def create_request_medical_records_definition(args):
        """
        Creates envelope definition for request medical records endpoint
        """
        #Update template tabs
        email = Email(
          tab_label="email", value=args["email"]
        )

        tabs = Tabs(
          email_tabs=[email] #, text_tabs=[date_signed]
        )

        # create the envelope definition
        envelope_definition = EnvelopeDefinition(
            status="sent",  # requests that the envelope be created and sent.
            template_id=args["template_id"],
            email_subject="Please sign this document"
        )
        # Create template role elements to connect the signer and cc recipients
        # to the template
        signer = TemplateRole(
            email=args["email"],
            name=args["name"],
            role_name="signer",
            tabs=tabs
        )

        # Add the TemplateRole objects to the envelope object
        envelope_definition.template_roles = [signer]
        return envelope_definition

    @staticmethod
    def create_covid_19_consent_form_definition(args):
        """
        Creates envelope definition for the covid-19 consent form endpoint
        """

        #Update template tabs
        first_name = Text(
          tab_label="first_name", value=args["first_name"]
        )
        last_name = Text(
          tab_label="last_name", value=args["last_name"]
        )
        email = Email(
          tab_label="email", value=args["email"]
        )
        phone_number = Text(
          tab_label="phone_number", value=f'{args["country_code"]}{args["phone_number"]}'
        )
        date_signed = Text(
          tab_label="date_signed", value=datetime.now().strftime("%m-%d-%Y")
        )

        tabs = Tabs(
          email_tabs=[email], text_tabs=[first_name, last_name, phone_number, date_signed]
        )

        phone_number = RecipientPhoneNumber(
            country_code=args["country_code"],
            number=args["phone_number"]
        )

        sms_notification = RecipientAdditionalNotification(
            phone_number=phone_number,
            secondary_delivery_method="SMS"
        )
        # Create template role elements to connect the signer to the template
        signer = TemplateRole(
            email=args["email"],
            name=f'{args["first_name"]} {args["last_name"]}',
            role_name="signer",
            tabs=tabs,
            additional_notifications=[sms_notification]
        )

        # create the envelope definition
        envelope_definition = EnvelopeDefinition(
            status="sent",  # requests that the envelope be created and sent.
            template_id=args["template_id"],
            email_subject="Please sign this document",
            template_roles = [signer]
        )

        return envelope_definition

    @staticmethod
    def create_application_for_participation_definition(args):
        """
        Creates envelope definition for endpoint: application for participation
        returns an envelope definition
        """
        #Update template tabs
        first_name = Text(
          tab_label="first_name", value=args["first_name"]
        )
        last_name = Text(
          tab_label="last_name", value=args["last_name"]
        )
        date_signed = Text(
          tab_label="date_signed", value=datetime.now().strftime("%m-%d-%Y")
        )

        tabs = Tabs(
          text_tabs=[first_name, last_name, date_signed]
        )

        # Create template role elements to connect the signer to the template
        signer = TemplateRole(
            email=args["email"],
            name=f'{args["first_name"]} {args["last_name"]}',
            role_name="signer",
            tabs=tabs,
            # Setting the client_user_id marks the signer as embedded
            client_user_id="1000"
        )
        # create the envelope definition
        envelope_definition = EnvelopeDefinition(
            status="sent",  # requests that the envelope be created and sent.
            template_id=args["template_id"],
            template_roles = [signer],
            email_subject="Please sign this document"
        )
        return envelope_definition

    @staticmethod
    def get_view_url(session, envelope_id, args):
        """
        Get the recipient view
        """

        # Create the recipient view request object
        recipient_view_request = RecipientViewRequest(
            authentication_method="None",
            client_user_id="1000",
            recipient_id="1",
            return_url=args["return_url"],
            user_name=f'{args["first_name"]} {args["last_name"]}',
            email=args["email"]
        )
        # Obtain the recipient view URL for the signing ceremony
        # Exceptions will be caught by the calling function
        ds_client = DsClient.get_configured_instance(session.get('access_token'))

        envelope_api = EnvelopesApi(ds_client)
        recipient_view = envelope_api.create_recipient_view(
            session.get('account_id'),
            envelope_id,
            recipient_view_request=recipient_view_request
        )
        return recipient_view.url
