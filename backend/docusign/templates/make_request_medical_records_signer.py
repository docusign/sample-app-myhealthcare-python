from docusign_esign import Signer, FullName, Text, Email, Tabs, SignHere, DateSigned, Checkbox, TabGroup

def make_request_medical_records_signer(workflow_id, args):
    """
    Create signer and fields using absolute positioning
    Add the tabs model to the signer
    """

    # Create the signer recipient model
    signer = Signer(
        role_name="signer",
        recipient_id="1",
        routing_order="1",
        delivery_method="email",
        identity_verification={"workflowId": workflow_id},
    )

    # Create fields
    full_name = FullName(
        document_id="1", page_number="1", x_position="347", y_position="150"
    )
    birth_date = Text(
        document_id="1", page_number="1", x_position="347", y_position="180",
        required="true", tab_label="birth_date", height="12", width="60",
        validation_message="Date format: mm-dd-yyyy",
        validation_pattern="^[0-9]{2}-[0-9]{2}-[0-9]{4}$"
    )
    email = Email(
        document_id="1", page_number="1", x_position="159", y_position="326",
        height="12", width="100", required="true", tab_label="email"
    )
    check1 = Checkbox(
        document_id="1", page_number="1", x_position="91", y_position="240",
        tab_label="check1", tab_group_labels=["release_purpose"], required="false"
    )
    check2 = Checkbox(
        document_id="1", page_number="1", x_position="175", y_position="240",
        tab_label="check2", tab_group_labels=["release_purpose"], required="false"
    )
    check3 = Checkbox(
        document_id="1", page_number="1", x_position="232", y_position="240",
        tab_label="check3", tab_group_labels=["release_purpose"], required="false"
    )
    check4 = Checkbox(
        document_id="1", page_number="1", x_position="323", y_position="240",
        tab_label="check4", tab_group_labels=["release_purpose"], required="false"
    )
    check5 = Checkbox(
        document_id="1", page_number="1", x_position="384", y_position="240",
        tab_label="check5", tab_group_labels=["release_purpose"], required="false"
    )
    check6 = Checkbox(
        document_id="1", page_number="1", x_position="429", y_position="240",
        tab_label="check6", tab_group_labels=["release_purpose"], required="false"
    )
    release_purpose_group = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="release_purpose"
    )
    check7 = Checkbox(
        document_id="1", page_number="1", x_position="91", y_position="297",
        tab_label="check7", tab_group_labels=["delivery_of_information"], required="false"
    )
    check8 = Checkbox(
        document_id="1", page_number="1", x_position="91", y_position="308",
        tab_label="check8", tab_group_labels=["delivery_of_information"], required="false"
    )
    check9 = Checkbox(
        document_id="1", page_number="1", x_position="91", y_position="330",
        tab_label="check9", tab_group_labels=["delivery_of_information"], required="false"
    )
    delivery_group = TabGroup(
        document_id="1", page_number="1", recipient_id="1", tab_scope="Document",
        group_rule="SelectExactly", minimum_required="1", maximum_allowed="1",
        group_label="delivery_of_information"
    )
    check10 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="427", tab_label="check10"
    )
    check11 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="437", tab_label="check11"
    )
    check12 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="447", tab_label="check12"
    )
    check13 = Checkbox(document_id="1", page_number="1",
        x_position="323", y_position="427", tab_label="check13"
    )
    check14 = Checkbox(document_id="1", page_number="1",
        x_position="323", y_position="438", tab_label="check14"
    )

    check15 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="475", tab_label="check15"
    )
    check16 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="486", tab_label="check16"
    )
    check17 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="496", tab_label="check17"
    )
    check18 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="507", tab_label="check18"
    )
    check19 = Checkbox(document_id="1", page_number="1",
        x_position="249", y_position="475", tab_label="check19"
    )
    check20 = Checkbox(document_id="1", page_number="1",
        x_position="249", y_position="486", tab_label="check20"
    )
    check21 = Checkbox(document_id="1", page_number="1",
        x_position="249", y_position="496", tab_label="check21"
    )
    check22 = Checkbox(document_id="1", page_number="1",
        x_position="249", y_position="507", tab_label="check22"
    )
    check23 = Checkbox(document_id="1", page_number="1",
        x_position="342", y_position="475", tab_label="check23"
    )
    check24 = Checkbox(document_id="1", page_number="1",
        x_position="342", y_position="486", tab_label="check24"
    )

    check25 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="533", tab_label="check25"
    )
    check26 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="543", tab_label="check26"
    )
    check27 = Checkbox(document_id="1", page_number="1",
        x_position="91", y_position="554", tab_label="check27"
    )
    check28 = Checkbox(document_id="1", page_number="1",
        x_position="232", y_position="533", tab_label="check28"
    )
    check29 = Checkbox(document_id="1", page_number="1",
        x_position="232", y_position="543", tab_label="check29"
    )
    check30 = Checkbox(document_id="1", page_number="1",
        x_position="232", y_position="554", tab_label="check30"
    )
    check31= Checkbox(document_id="1", page_number="1",
        x_position="385", y_position="533", tab_label="check31"
    )

    sign_here = SignHere(
        document_id="1", page_number="1", x_position="181", y_position="682"
    )
    date_signed = DateSigned(
        document_id="1", page_number="1", x_position="399", y_position="697"
    )

    # The Tabs object requires arrays of the different field/tab types
    signer.tabs = Tabs(
        full_name_tabs=[full_name],
        text_tabs=[birth_date],
        email_tabs=[email],
        checkbox_tabs=[
            check1, check2, check3, check4, check5, check6,
            check7, check8, check9,
            check10, check11, check12, check13, check14,
            check15, check16, check17, check18, check19,
            check20, check21, check22, check23, check24,
            check25, check26, check27, check28, check29,
            check30, check31
        ],
        tab_groups=[release_purpose_group, delivery_group],
        sign_here_tabs=[sign_here],
        date_signed_tabs=[date_signed]
    )
    return signer
