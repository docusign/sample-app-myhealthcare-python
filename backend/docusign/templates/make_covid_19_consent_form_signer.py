from datetime import datetime
from docusign_esign import Signer, Text, Email, Tabs, SignHere, Checkbox, TabGroup

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
        tab_group_labels=["yn1"], required="false", x_position="478", y_position="246",
    )
    check2 = Checkbox(
        document_id="1", page_number="1", tab_label="check2",
        tab_group_labels=["yn1"], required="false", x_position="526", y_position="246",
    )
    yn1 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn1"
    )

    check3 = Checkbox(
        document_id="1", page_number="1", tab_label="check3",
        tab_group_labels=["yn2"], required="false", x_position="478", y_position="267",
    )
    check4 = Checkbox(
        document_id="1", page_number="1", tab_label="check4",
        tab_group_labels=["yn2"], required="false", x_position="526", y_position="267",
    )
    yn2 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn2"
    )

    check5 = Checkbox(
        document_id="1", page_number="1", tab_label="check5",
        tab_group_labels=["yn3"], required="false", x_position="478", y_position="294",
    )
    check6 = Checkbox(
        document_id="1", page_number="1", tab_label="check6",
        tab_group_labels=["yn3"], required="false", x_position="526", y_position="294",
    )
    yn3 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn3"
    )

    check7 = Checkbox(
        document_id="1", page_number="1", tab_label="check7",
        tab_group_labels=["yn4"], required="false", x_position="478", y_position="325",
    )
    check8 = Checkbox(
        document_id="1", page_number="1", tab_label="check8",
        tab_group_labels=["yn4"], required="false", x_position="526", y_position="325",
    )
    yn4 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn4"
    )

    check9 = Checkbox(
        document_id="1", page_number="1", tab_label="check9",
        tab_group_labels=["yn5"], required="false", x_position="478", y_position="357",
    )
    check10 = Checkbox(
        document_id="1", page_number="1", tab_label="check10",
        tab_group_labels=["yn5"], required="false", x_position="526", y_position="357",
    )
    yn5 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn5"
    )

    check11 = Checkbox(
        document_id="1", page_number="1", tab_label="check11",
        tab_group_labels=["yn6"], required="false", x_position="478", y_position="390",
    )
    check12 = Checkbox(
        document_id="1", page_number="1", tab_label="check12",
        tab_group_labels=["yn6"], required="false", x_position="526", y_position="390",
    )
    yn6 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn6"
    )

    check13 = Checkbox(
        document_id="1", page_number="1", tab_label="check13",
        tab_group_labels=["yn7"], required="false", x_position="478", y_position="417",
    )
    check14 = Checkbox(
        document_id="1", page_number="1", tab_label="check14",
        tab_group_labels=["yn7"], required="false", x_position="526", y_position="417",
    )
    yn7 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn7"
    )

    check15 = Checkbox(
        document_id="1", page_number="1", tab_label="check15",
        tab_group_labels=["yn8"], required="false", x_position="478", y_position="444",
    )
    check16 = Checkbox(
        document_id="1", page_number="1", tab_label="check16",
        tab_group_labels=["yn8"], required="false", x_position="526", y_position="444",
    )
    yn8 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn8"
    )

    check17 = Checkbox(
        document_id="1", page_number="1", tab_label="check17",
        tab_group_labels=["yn9"], required="false", x_position="478", y_position="471",
    )
    check18 = Checkbox(
        document_id="1", page_number="1", tab_label="check18",
        tab_group_labels=["yn9"], required="false", x_position="526", y_position="471",
    )
    yn9 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn9"
    )

    check19 = Checkbox(
        document_id="1", page_number="1", tab_label="check19",
        tab_group_labels=["yn10"], required="false", x_position="478", y_position="492",
    )
    check20 = Checkbox(
        document_id="1", page_number="1", tab_label="check20",
        tab_group_labels=["yn10"], required="false", x_position="526", y_position="492",
    )
    yn10 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn10"
    )

    check21 = Checkbox(
        document_id="1", page_number="1", tab_label="check21",
        tab_group_labels=["yn11"], required="false", x_position="478", y_position="513",
    )
    check22 = Checkbox(
        document_id="1", page_number="1", tab_label="check22",
        tab_group_labels=["yn11"], required="false", x_position="526", y_position="513",
    )
    yn11 = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="yn11"
    )

    first_dose_date = Text(
        document_id="1", page_number="1", required="false", tab_label="first_dose_date",
        height="12", width="60", x_position="488", y_position="533",
        validation_message="Date format: mm-dd-yyyy",
        validation_pattern="^[0-9]{2}-[0-9]{2}-[0-9]{4}$"
    )
    first_dose_name = Text(
        document_id="1", page_number="1", required="false", tab_label="first_dose_name",
        height="12", width="60", x_position="488", y_position="554"
    )

    sign_here = SignHere(
        document_id="1", page_number="1",
        anchor_string="/Patient", anchor_units="pixels", anchor_x_offset="32"
    )
    date_signed = Text(
        document_id="1", page_number="1", required="true", tab_label="date_signed",
        locked="true", x_position="500", y_position="666"
    )

    # The Tabs object requires arrays of the different field/tab types
    signer.tabs = Tabs(
        text_tabs=[
            last_name, first_name, birth_date, date_signed, address, phone_number,
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
        sign_here_tabs=[sign_here]
    )
    return signer
