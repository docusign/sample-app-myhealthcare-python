from datetime import datetime
from docusign_esign import Signer, CarbonCopy, Text, Number, Tabs, SignHere, SignerAttachment

def make_application_for_participation_signer(args):
    """
    Create signer and fields using absolute positioning
    Add the tabs model to the signer
    """

    # Create the signer recipient model
    signer = Signer(
        role_name="signer",
        recipient_id="1",
        routing_order="1"
    )

    # Create fields
    last_name = Text(
        document_id="1", page_number="1", x_position="73", y_position="143",
        required="true", tab_label="last_name", height="12", width="60"
    )
    first_name = Text(
        document_id="1", page_number="1", x_position="232", y_position="143",
        required="true", tab_label="first_name", height="12", width="60"
    )
    ssn1 = Text(
        document_id="1", page_number="1", x_position="392", y_position="154",
        required="true", tab_label="ssn1", height="12", width="40",
        validation_message="3 digits",
        validation_pattern="^[0-9]{3}$"
    )
    ssn2 = Text(
        document_id="1", page_number="1", x_position="449", y_position="154",
        required="true", tab_label="ssn2", height="12", width="30",
        validation_message="2 digits",
        validation_pattern="^[0-9]{2}$"
    )
    ssn3 = Text(
        document_id="1", page_number="1", x_position="489", y_position="154",
        required="true", tab_label="ssn3", height="12", width="60",
        validation_message="4 digits",
        validation_pattern="^[0-9]{4}$"
    )
    address = Text(
        document_id="1", page_number="1", x_position="41", y_position="241",
        required="true", tab_label="address", height="12", width="320"
    )

    phone1 = Number(
        document_id="1", page_number="1", x_position="395", y_position="242",
        required="true", tab_label="phone1", height="12", width="30"
    )
    phone2 = Number(
        document_id="1", page_number="1", x_position="451", y_position="242",
        required="true", tab_label="phone2", height="12", width="40"
    )
    phone3 = Number(
        document_id="1", page_number="1", x_position="507", y_position="242",
        required="true", tab_label="phone3", height="12", width="60"
    )

    family_size = Number(
        document_id="1", page_number="1", x_position="395", y_position="290",
        required="true", tab_label="family_size", height="12", width="30"
    )


    last_12 = Text(
        document_id="1", page_number="2", x_position="40", y_position="214",
        required="true", tab_label="last_12", height="12", width="80"
    )

    attachment = SignerAttachment(
        document_id="1", page_number="2", x_position="3", y_position="737",
        optional='true'
    )

    sign_here = SignHere(
        document_id="1", page_number="2", x_position="225", y_position="728"
    )

    date_signed = Text(
        document_id="1", page_number="2", x_position="458", y_position="746",
        required="true", tab_label="date_signed", height="12", width="60",
        locked="true"
    )

    # The Tabs object requires arrays of the different field/tab types
    signer.tabs = Tabs(
        text_tabs=[last_name, first_name, ssn1, ssn2, ssn3, address, last_12, date_signed],
        number_tabs=[phone1, phone2, phone3, family_size],
        signer_attachment_tabs=[attachment],
        sign_here_tabs=[sign_here],
    )
    return signer
