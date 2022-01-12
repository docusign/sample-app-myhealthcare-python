from datetime import datetime
from docusign_esign import Signer, Text, Email, Tabs, SignHere, DateSigned, Checkbox, TabGroup

def make_covid_19_consent_form_signer(args):
    """
    Create signer and fields using anchor positioning
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
        document_id="1", page_number="1", required="true", tab_label="last_name",
        height="12", width="60",
        anchor_string="Last Name", anchor_units="pixels", anchor_y_offset="12"
    )
    first_name = Text(
        document_id="1", page_number="1", required="true", tab_label="first_name",
        height="12", width="60",
        anchor_string="First Name", anchor_units="pixels", anchor_y_offset="12"
    )
    birth_date = Text(
        document_id="1", page_number="1", required="true", tab_label="birth_date",
        height="12", width="60",
        anchor_string="Date of Birth", anchor_units="pixels", anchor_y_offset="12",
        validation_message="Date format: mm-dd-yyyy",
        validation_pattern="^[0-9]{2}-[0-9]{2}-[0-9]{4}$"
    )
    address = Text(
        document_id="1", page_number="1", required="true", tab_label="address",
        height="12", width="270",
        anchor_string="Address", anchor_units="pixels", anchor_y_offset="12"
    )
    city = Text(
        document_id="1", page_number="1", required="true", tab_label="city",
        height="12", width="150",
        anchor_string="City", anchor_units="pixels", anchor_y_offset="12"
    )
    state = Text(
        document_id="1", page_number="1", required="true", tab_label="state",
        height="12", width="30",
        anchor_string="State", anchor_units="pixels", anchor_y_offset="12"
    )
    zip = Text(
        document_id="1", page_number="1", required="true", tab_label="zip",
        height="12", width="60",
        anchor_string="Zip", anchor_units="pixels", anchor_y_offset="12"
    )
    phone_number = Text(
        document_id="1", page_number="1", required="true", tab_label="phone_number",
        height="12", width="150",
        anchor_string="Phone Number", anchor_units="pixels", anchor_y_offset="12"
    )
    email = Email(
        document_id="1", page_number="1", required="true", tab_label="email",
        height="12", width="150",
        anchor_string="Email", anchor_units="pixels", anchor_y_offset="12"
    )

    check1 = Checkbox(
        document_id="1", page_number="1", tab_label="check1",
        tab_group_labels=["yn1"], required="false", x_position="503", y_position="73",
    )
    check2 = Checkbox(
        document_id="1", page_number="1", tab_label="check2",
        tab_group_labels=["yn1"], required="false", x_position="503", y_position="91",
    )
    yn1 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn1"
    )

    check3 = Checkbox(
        document_id="1", page_number="1", tab_label="check3",
        tab_group_labels=["yn2"], required="false", x_position="471", y_position="234",
    )
    check4 = Checkbox(
        document_id="1", page_number="1", tab_label="check4",
        tab_group_labels=["yn2"], required="false", x_position="528", y_position="234",
    )
    yn2 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn2"
    )

    check5 = Checkbox(
        document_id="1", page_number="1", tab_label="check5",
        tab_group_labels=["yn3"], required="false", x_position="471", y_position="282",
    )
    check6 = Checkbox(
        document_id="1", page_number="1", tab_label="check6",
        tab_group_labels=["yn3"], required="false", x_position="528", y_position="282",
    )
    yn3 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn3"
    )

    check7 = Checkbox(
        document_id="1", page_number="1", tab_label="check7",
        tab_group_labels=["yn4"], required="false", x_position="471", y_position="309",
    )
    check8 = Checkbox(
        document_id="1", page_number="1", tab_label="check8",
        tab_group_labels=["yn4"], required="false", x_position="528", y_position="309",
    )
    yn4 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn4"
    )

    check9 = Checkbox(
        document_id="1", page_number="1", tab_label="check9",
        tab_group_labels=["yn5"], required="false", x_position="471", y_position="345",
    )
    check10 = Checkbox(
        document_id="1", page_number="1", tab_label="check10",
        tab_group_labels=["yn5"], required="false", x_position="528", y_position="345",
    )
    yn5 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn5"
    )

    check11 = Checkbox(
        document_id="1", page_number="1", tab_label="check11",
        tab_group_labels=["yn6"], required="false", x_position="471", y_position="382",
    )
    check12 = Checkbox(
        document_id="1", page_number="1", tab_label="check12",
        tab_group_labels=["yn6"], required="false", x_position="528", y_position="382",
    )
    yn6 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn6"
    )

    check13 = Checkbox(
        document_id="1", page_number="1", tab_label="check13",
        tab_group_labels=["yn7"], required="false", x_position="471", y_position="417",
    )
    check14 = Checkbox(
        document_id="1", page_number="1", tab_label="check14",
        tab_group_labels=["yn7"], required="false", x_position="528", y_position="417",
    )
    yn7 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn7"
    )

    check15 = Checkbox(
        document_id="1", page_number="1", tab_label="check15",
        tab_group_labels=["yn8"], required="false", x_position="471", y_position="441",
    )
    check16 = Checkbox(
        document_id="1", page_number="1", tab_label="check16",
        tab_group_labels=["yn8"], required="false", x_position="528", y_position="441",
    )
    yn8 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn8"
    )

    check17 = Checkbox(
        document_id="1", page_number="1", tab_label="check17",
        tab_group_labels=["yn9"], required="false", x_position="471", y_position="465",
    )
    check18 = Checkbox(
        document_id="1", page_number="1", tab_label="check18",
        tab_group_labels=["yn9"], required="false", x_position="528", y_position="465",
    )
    yn9 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn9"
    )

    check19 = Checkbox(
        document_id="1", page_number="1", tab_label="check19",
        tab_group_labels=["yn10"], required="false", x_position="471", y_position="489",
    )
    check20 = Checkbox(
        document_id="1", page_number="1", tab_label="check20",
        tab_group_labels=["yn10"], required="false", x_position="528", y_position="489",
    )
    yn10 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn10"
    )

    check21 = Checkbox(
        document_id="1", page_number="1", tab_label="check21",
        tab_group_labels=["yn11"], required="false", x_position="471", y_position="513",
    )
    check22 = Checkbox(
        document_id="1", page_number="1", tab_label="check22",
        tab_group_labels=["yn11"], required="false", x_position="528", y_position="513",
    )
    yn11 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn11"
    )

    first_dose_date = Text(
        document_id="1", page_number="1", required="false", tab_label="first_dose_date",
        height="12", width="60", x_position="470", y_position="537",
        validation_message="Date format: mm-dd-yyyy",
        validation_pattern="^[0-9]{2}-[0-9]{2}-[0-9]{4}$"
    )
    first_dose_name = Text(
        document_id="1", page_number="1", required="false", tab_label="first_dose_name",
        height="12", width="60", x_position="470", y_position="562"
    )

    sign_here = SignHere(
        document_id="1", page_number="1", x_position="102", y_position="707"
    )
    date_signed = DateSigned(
        document_id="1", page_number="1", x_position="443", y_position="718"
    )

    # The Tabs object requires arrays of the different field/tab types
    signer.tabs = Tabs(
        text_tabs=[
            last_name, first_name, birth_date, address, city, state, zip, phone_number,
            first_dose_date, first_dose_name
        ],
        email_tabs=[email],
        checkbox_tabs=[
            check1, check2,
            check3, check4,
            check5, check6,
            check7, check8,
            check9, check10,
            check11, check12,
            check13, check14,
            check15, check16,
            check17, check18,
            check19, check20,
            check21, check22
        ],
        tab_groups=[yn1, yn2, yn3, yn4, yn5, yn6, yn7, yn8, yn9, yn10, yn11],
        sign_here_tabs=[sign_here],
        date_signed_tabs=[date_signed]
    )
    return signer
