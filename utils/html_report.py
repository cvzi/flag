from typing import Optional
from pathlib import Path

try:
    import flag
except ModuleNotFoundError:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    import flag


def truthy(key: str, v: Optional[bool]) -> str:
    return (
        f'<abbr title="{key} = True">✅</abbr>'
        if v
        else (
            f'<abbr title="{key} = None">❓</abbr>'
            if v is None
            else f'<abbr title="{key} = False">❌</abbr>'
        )
    )


if __name__ == "__main__":
    all_flags = flag.infos(extended=True)

    all_flags = dict(
        sorted(
            all_flags.items(),
            key=lambda t: f"{not t[1]['supported']}{'comment' not in t[1]}{t[1]['id_status']}{not t[1]['valid']}{t[0]}",
        )
    )


    path = Path(__file__).parent.parent.joinpath("docs/_static/report.html")

    print("Writing html report to", path)

    with open(path, "w") as f:
        f.write('<!DOCTYPE html><html lang="en-US">\n')
        f.write(
            '<head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        )
        f.write("<style>\n")
        f.write("div {padding:3px}\n")
        f.write("th {border: 2px solid #0003; border-bottom: 0px;}\n")
        f.write("td {border: 2px solid #0002; border-left: 0px; border-right: 0px; border-bottom: 0px;}\n")
        f.write(".sup {background:white}\n")
        f.write(".sup:nth-child(even) {background:white}\n")
        f.write(".no_sup {background: #3b88c3}\n")
        f.write("</style>\n")
        f.write("</head><body>\n")
        f.write(
            '<div> <a href="https://flag.readthedocs.io/en/latest/">&larr; back to the package Documentation</a></div>\n'
        )
        f.write("<h1>Unicode flags</h1>\n")

        f.write("""<div>The following table is based on data from
<a href="https://github.com/unicode-org/cldr/blob/main/common/validity/region.xml">region.xml</a>
and
<a href="https://github.com/unicode-org/cldr/blob/main/common/validity/subdivision.xml">subdivision.xml
</a> from the <a href="https://cldr.unicode.org/">Unicode CLDR Project</a>.<br>
Validity of the flags is based on the
<a href ="https://www.unicode.org/reports/tr51/#Flags">Unicode Emoji Standard</a>.<br>
Support of the flags is based on manual inspection of the flags in popular browsers and cell phones.<br>
This file can be generated with the script at
<a href="https://github.com/cvzi/flag/blob/main/utils/html_report.py">https://github.com/cvzi/flag/blob/main/utils/html_report.py</a>.<br>
</div>\n""")
        f.write(
            '<div>Lines with <span class="no_sup">blue background</span> are unsupported flags.</div>\n'
        )
        f.write("<div>You are encouraged to inspect the flags on multiple platforms to spot mistakes.</div>\n")

        f.write("<table>\n")

        f.write("  <tr>")
        f.write("    <th>🏳‍🌈</th>")
        f.write("    <th>ⱯZ</th>")
        for key in ["id_status", "valid", "supported", "comment"]:
            f.write(f"    <th>{key}</th>")
        f.write("  </tr>\n")

        for seq, data in all_flags.items():
            f.write(f'  <tr class="{"sup" if data["supported"] else "no_sup" }">')
            f.write(f"    <td>{flag.flag(seq)}</td>")
            f.write(f"    <td>{seq}</td>")
            for key in ["id_status", "valid", "supported", "comment"]:
                if key not in data:
                    f.write("    <td></td>")
                else:
                    value = data[key]
                    if isinstance(value, bool) or value is None:
                        f.write(f"    <td>{truthy(key, value)}</td>")
                    else:
                        f.write(f"    <td>{value}</td>")
            f.write("  </tr>\n")
        f.write("</table>\n")
        f.write("</body></html>\n")
