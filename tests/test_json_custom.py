import json
from io import StringIO
from rich.json import JSON
from rich.console import Console


def test_json_rendering_basic():
    # Primer podataka
    data = {
        "ime": "Jovan",
        "godine": 28,
        "jezici": ["Python", "C++"]
    }

    # Pretvaramo u JSON string
    json_string = json.dumps(data)

    # Kreiramo Rich JSON objekat
    json_obj = JSON(json_string)

    # Hvatamo output konzole
    output = StringIO()
    console = Console(file=output, force_terminal=True, color_system=None)

    console.print(json_obj)

    rendered = output.getvalue()

    # Proveravamo da li se vrednosti pojavljuju u ispisu
    assert "Jovan" in rendered
    assert "28" in rendered
    assert "Python" in rendered
    assert "C++" in rendered