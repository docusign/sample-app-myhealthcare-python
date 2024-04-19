import base64
import os

from docusign_esign import Document

def create_document(doc_file):
    """
    Create the document model
    """

    demo_docs_path = os.path.abspath(
        os.path.join(os.path.dirname(os.curdir), 'docusign', 'pdf')
    )

    with open(os.path.join(demo_docs_path, doc_file), "rb") as file:
        content_bytes = file.read()
    base64_file_content = base64.b64encode(content_bytes).decode("ascii")

    name, file_extension = doc_file.split('.')

    return Document(  # create the Docusign document object
        document_base64=base64_file_content,
        name=name,  # can be different from actual file name
        file_extension=file_extension,  # many different document types are accepted
        document_id=1  # a label used to reference the doc
    )
