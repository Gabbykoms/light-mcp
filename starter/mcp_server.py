from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc

@mcp.tool()
def read_doc(doc_id:str):
    """
    Docstring for read_doc
    
    :param doc_id: Description
    :type doc_id: str
    """
    if doc_id not in docs:
        raise ValueError(f"Dcoument {doc_id} not found in docs")
    return docs[doc_id]


# TODO: Write a tool to edit a doc
@mcp.tool()
def edit_doc(doc_id:str, old_text : str, new_text : str) -> str:
    """
    Docstring for edit_doc
    
    :param doc_id: Description
    :type doc_id: str
    :param old_text: Description
    :type old_text: str
    :param new_text: Description
    :type new_text: str
    :return: Description
    :rtype: str
    """
    if doc_id not in docs:
        raise ValueError(f"Dcoument {doc_id} not found in docs")
    
    if not new_text:
        raise ValueError ("new text must not be empty")

    if old_text not in docs[doc_id]:
        raise ValueError(f"text not found in document : {doc_id}")

    docs[doc_id] = docs[doc_id].replace(old_text, new_text)
    return f"Updated document : {doc_id}"


# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
