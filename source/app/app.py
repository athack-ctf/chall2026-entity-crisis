from flask import Flask, render_template, request, Response
from lxml import etree

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="styles",
    static_url_path="/styles",
)


def parse_availability_xml(xml_bytes: bytes) -> dict:
    if not isinstance(xml_bytes, (bytes, bytearray)):
        raise TypeError("xml_bytes must be bytes")

    if len(xml_bytes) > 10_000:
        raise ValueError("XML payload too large")

    parser = etree.XMLParser(
        resolve_entities=True,
        load_dtd=True,
        no_network=False,
        huge_tree=False,
        remove_comments=True,
        remove_pis=True,
        recover=False,
    )

    try:
        root = etree.fromstring(xml_bytes, parser)
    except etree.XMLSyntaxError as e:
        raise ValueError(f"Bad XML: {e}") from e

    item = (root.findtext("item") or "").strip()
    return {"root": root.tag, "item": item}


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/stock")
def stock():
    ct = request.headers.get("Content-Type", "")
    if "xml" not in ct.lower():
        return Response("Expected XML", status=415, mimetype="text/plain")

    xml_body = request.get_data(cache=False)

    try:
        out = parse_availability_xml(xml_body)
    except ValueError as e:
        return Response(str(e), status=400, mimetype="text/plain")
    except Exception as e:
        return Response(f"Server error: {e}", status=500, mimetype="text/plain")

    if (out.get("item") != "@hack-flag"):
        return Response("Invalid item: " + out.get("item"), status=400, mimetype="text/plain")

    return Response("IN STOCK: " + str(out), status=200, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
