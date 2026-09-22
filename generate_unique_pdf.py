# generate_unique_pdf.py
import subprocess
import os

html_template = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Lab Practical Submission - Khatri Om Kumar</title>
<style>
    @page {
        size: A4;
        margin: 14mm 16mm 14mm 16mm;
    }
    * {
        box-sizing: border-box;
    }
    body {
        font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
        font-size: 10.2pt;
        line-height: 1.4;
        color: #111;
        background: #fff;
        margin: 0;
        padding: 0;
    }
    .page {
        page-break-after: always;
        height: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 265mm;
    }
    .page:last-child {
        page-break-after: avoid;
    }

    /* Page Footer Line */
    .page-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 8.5pt;
        color: #666666;
        border-top: 1px solid #d0d0d0;
        padding-top: 5px;
        margin-top: auto;
    }
    .footer-left {
        font-weight: 600;
        color: #444444;
    }
    .footer-right {
        color: #666666;
    }

    /* Cover Page Styling (Clean White University Theme) */
    .cover-page {
        background-color: #ffffff;
        color: #111111;
        padding: 40px 30px;
        min-height: 260mm;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        border: 1px solid #d0d0d0;
    }
    .corner-tl { position: absolute; top: 20px; left: 20px; width: 25px; height: 25px; border-top: 2px solid #888; border-left: 2px solid #888; }
    .corner-tr { position: absolute; top: 20px; right: 20px; width: 25px; height: 25px; border-top: 2px solid #888; border-right: 2px solid #888; }
    .corner-bl { position: absolute; bottom: 20px; left: 20px; width: 25px; height: 25px; border-bottom: 2px solid #888; border-left: 2px solid #888; }
    .corner-br { position: absolute; bottom: 20px; right: 20px; width: 25px; height: 25px; border-bottom: 2px solid #888; border-right: 2px solid #888; }

    .cover-univ {
        text-align: center;
        margin-top: 30px;
    }
    .cover-univ h2 {
        font-size: 14pt;
        letter-spacing: 1.2px;
        margin: 0 0 8px 0;
        color: #222222;
        font-weight: 700;
    }
    .cover-univ h3 {
        font-size: 11pt;
        letter-spacing: 0.8px;
        margin: 0 0 5px 0;
        color: #8c5338;
        font-weight: 600;
    }
    .cover-univ h4 {
        font-size: 10pt;
        letter-spacing: 0.6px;
        margin: 0;
        color: #8c5338;
        font-weight: 600;
    }
    .cover-divider {
        width: 90%;
        height: 1px;
        background: #cccccc;
        margin: 25px auto;
    }
    .cover-title {
        text-align: center;
        margin: 20px 0 35px 0;
    }
    .cover-title h1 {
        font-size: 20pt;
        letter-spacing: 2px;
        color: #333333;
        margin: 0 0 10px 0;
        font-weight: 700;
    }
    .cover-title h2 {
        font-size: 14pt;
        letter-spacing: 1.2px;
        color: #444444;
        margin: 0 0 8px 0;
        font-weight: 600;
    }
    .cover-title p {
        font-size: 10.5pt;
        color: #666666;
        margin: 0;
    }
    .cover-table-container {
        background: #ffffff;
        border: 1px solid #d8d8d8;
        border-radius: 4px;
        overflow: hidden;
        margin: 0 15px 40px 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .cover-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 10.5pt;
    }
    .cover-table td {
        padding: 13px 20px;
        border-bottom: 1px solid #e8e8e8;
    }
    .cover-table tr:last-child td {
        border-bottom: none;
    }
    .cover-table td.label {
        font-weight: 700;
        color: #1e3a8a;
        width: 34%;
    }
    .cover-table td.val {
        font-weight: 600;
        color: #111111;
    }

    /* Content Typography */
    h1.doc-title {
        font-size: 13.5pt;
        font-weight: bold;
        margin: 0 0 4px 0;
        color: #000;
    }
    h2.doc-subtitle {
        font-size: 11.5pt;
        font-weight: bold;
        margin: 0 0 10px 0;
        color: #000;
    }
    h2.sec-heading {
        font-size: 11.5pt;
        font-weight: bold;
        margin: 10px 0 6px 0;
        color: #000;
    }
    p {
        margin: 3px 0;
    }
    .arrow-bullet {
        margin: 3px 0;
        padding-left: 8px;
    }

    /* Code Card (VS Code Dark Theme) */
    .code-card {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 11px 15px;
        font-family: Consolas, "Courier New", monospace;
        font-size: 8.7pt;
        line-height: 1.34;
        white-space: pre-wrap;
        margin: 6px 0 10px 0;
        border-radius: 3px;
    }
    .kw { color: #c586c0; }       /* def, return, import, from */
    .kw-c { color: #569cd6; }     /* if, for, while, in, not */
    .fn { color: #dcdcaa; }       /* function names */
    .st { color: #ce9178; }       /* strings */
    .cm { color: #6a9955; }       /* comments */
    .num { color: #b5cea8; }      /* numbers */

    /* Terminal Screenshot Card */
    .terminal-card {
        margin: 6px 0 10px 0;
        background-color: #1e1e1e;
        border: 1px solid #333333;
        border-radius: 4px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.18);
    }
    .terminal-tabs {
        background-color: #252526;
        display: flex;
        align-items: center;
        gap: 18px;
        padding: 5px 14px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 8pt;
        color: #969696;
        border-bottom: 1px solid #1e1e1e;
        white-space: nowrap;
    }
    .terminal-tab-active {
        color: #ffffff;
        position: relative;
        font-weight: 600;
    }
    .terminal-tab-active::after {
        content: "";
        position: absolute;
        bottom: -6px;
        left: 0;
        right: 0;
        height: 2px;
        background-color: #007acc;
    }
    .terminal-body {
        background-color: #181818;
        color: #cccccc;
        font-family: Consolas, "Courier New", monospace;
        font-size: 8.5pt;
        line-height: 1.36;
        padding: 8px 14px;
        white-space: pre-wrap;
        word-break: break-word;
    }
    .ps-path {
        color: #e6edf3;
    }
    .ps-cmd {
        color: #3fb950;
        font-weight: 500;
    }
    .ps-cursor {
        display: inline-block;
        background: #ffffff;
        color: #181818;
        font-weight: bold;
        line-height: 1;
    }
</style>
</head>
<body>

<!-- ================= COVER PAGE ================= -->
<div class="page">
    <div class="cover-page">
        <div class="corner-tl"></div>
        <div class="corner-tr"></div>
        <div class="corner-bl"></div>
        <div class="corner-br"></div>

        <div class="cover-univ">
            <h2>THE MAHARAJA SAYAJIRAO UNIVERSITY OF BARODA</h2>
            <h3>FACULTY OF TECHNOLOGY AND ENGINEERING</h3>
            <h4>DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING</h4>
        </div>

        <div class="cover-divider"></div>

        <div class="cover-title">
            <h1>LABORATORY WORK SUBMISSION</h1>
            <h2>ARTIFICIAL INTELLIGENCE (AI)</h2>
            <p>Academic Year: 2026 – 2027</p>
        </div>

        <div class="cover-table-container">
            <table class="cover-table">
                <tr>
                    <td class="label">Student Name:</td>
                    <td class="val">KHATRI OM KUMAR</td>
                </tr>
                <tr>
                    <td class="label">PRN:</td>
                    <td class="val">8024056707</td>
                </tr>
                <tr>
                    <td class="label">Roll No:</td>
                    <td class="val">36</td>
                </tr>
                <tr>
                    <td class="label">Class:</td>
                    <td class="val">BE-III (GIA)</td>
                </tr>
                <tr>
                    <td class="label">Branch:</td>
                    <td class="val">Computer Science & Engineering</td>
                </tr>
                <tr>
                    <td class="label">Subject:</td>
                    <td class="val">Artificial Intelligence (AI)</td>
                </tr>
            </table>
        </div>
    </div>
</div>

<!-- ================= PAGE 1 ================= -->
<div class="page">
    <div class="content-body">
        <h1 class="doc-title">Practical 1, 2, 3: Implement Search Algorithms (3 weeks)</h1>
        <h2 class="doc-subtitle">Path Finding on a City Map</h2>
        
        <p>1. Check the cities.py file. That is the map of the cites</p>
        <p class="arrow-bullet">➔ graph = {</p>

        <div class="code-card"> "Ahmedabad":[("Vadodara",110),("Rajkot",215),("Udaipur",260),("Indore",400)],
 "Vadodara":[("Ahmedabad",110),("Surat",155),("Indore",390),("Udaipur",330)],
 "Surat":[("Vadodara",155),("Mumbai",285),("Nashik",260)],
 "Mumbai":[("Surat",285),("Nashik",170),("Pune",150)],
 "Pune":[("Mumbai",150),("Nashik",210),("Solapur",250),("Hyderabad",560)],
 
 "Nashik":[("Mumbai",170),("Surat",260),("Pune",210),("Aurangabad",180),("Indore",420
)],
 "Aurangabad":[("Nashik",180),("Nagpur",480),("Hyderabad",560),("Indore",410)],
 "Rajkot":[("Ahmedabad",215),("Bhuj",230)],
 "Bhuj":[("Rajkot",230),("Ahmedabad",335)],
 
 "Udaipur":[("Ahmedabad",260),("Vadodara",330),("Jaipur",395),("Indore",385),("Kota",2
85)],
 "Jaipur":[("Udaipur",395),("Delhi",280),("Agra",240),("Kota",250)],
 "Delhi":[("Jaipur",280),("Agra",233),("Chandigarh",245),("Lucknow",555)],
 "Agra":[("Delhi",233),("Jaipur",240),("Gwalior",120),("Kanpur",285)],
 "Gwalior":[("Agra",120),("Jhansi",100),("Bhopal",420)],
 "Jhansi":[("Gwalior",100),("Bhopal",330),("Kanpur",220)],
 "Kanpur":[("Agra",285),("Jhansi",220),("Lucknow",90),("Prayagraj",200)],
 "Lucknow":[("Delhi",555),("Kanpur",90),("Prayagraj",200),("Varanasi",315)],
 "Prayagraj":[("Kanpur",200),("Lucknow",200),("Varanasi",125)],
 "Varanasi":[("Prayagraj",125),("Lucknow",315),("Patna",255)],
 "Patna":[("Varanasi",255),("Ranchi",330),("Kolkata",585)],
 "Ranchi":[("Patna",330),("Kolkata",400),("Raipur",560)],
 "Kolkata":[("Patna",585),("Ranchi",400),("Bhubaneswar",440)],
 "Bhubaneswar":[("Kolkata",440),("Visakhapatnam",440),("Raipur",530)],</div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 1 of 7</span>
    </div>
</div>

<!-- ================= PAGE 2 ================= -->
<div class="page">
    <div class="content-body">
        <div class="code-card"> "Visakhapatnam":[("Bhubaneswar",440),("Vijayawada",350),("Hyderabad",620)],
 "Vijayawada":[("Visakhapatnam",350),("Hyderabad",275),("Chennai",450)],
 
 "Hyderabad":[("Pune",560),("Aurangabad",560),("Nagpur",500),("Vijayawada",275),("Be
ngaluru",570),("Chennai",630),("Visakhapatnam",620)],
 
 "Nagpur":[("Indore",445),("Bhopal",350),("Aurangabad",480),("Hyderabad",500),("Raipu
r",285)],
 
 "Indore":[("Ahmedabad",400),("Vadodara",390),("Udaipur",385),("Bhopal",195),("Nagpu
r",445),("Nashik",420),("Aurangabad",410)],
 "Bhopal":[("Indore",195),("Nagpur",350),("Jhansi",330),("Gwalior",420)],
 "Raipur":[("Nagpur",285),("Ranchi",560),("Bhubaneswar",530)],
 "Chandigarh":[("Delhi",245)],
 "Kota":[("Jaipur",250),("Udaipur",285)],
 "Bengaluru":[("Hyderabad",570),("Chennai",345)],
 "Chennai":[("Bengaluru",345),("Vijayawada",450),("Hyderabad",630)],
 "Solapur":[("Pune",250)]
}</div>

        <p class="arrow-bullet">➔ Print the path, total cost.</p>
        <p class="arrow-bullet">➔ Track and print the number of nodes explored for each algorithm during 
the entire search process (this gives you an estimate of the time 
complexity) and also track and print the maximum number of nodes 
stored in the Queue/Stack at any point in time (this gives you an 
estimate of the space complexity).</p>
        <br>
        <h2 class="sec-heading">2. Implement BFS</h2>

        <div class="code-card"><span class="kw">from</span> collections <span class="kw">import</span> deque
<span class="kw">from</span> city_map <span class="kw">import</span> road_network</div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 2 of 7</span>
    </div>
</div>

<!-- ================= PAGE 3 ================= -->
<div class="page">
    <div class="content-body">
        <div class="code-card"><span class="kw">def</span> <span class="fn">calculate_cost</span>(route):
    total_dist = <span class="num">0</span>
    <span class="kw-c">for</span> k <span class="kw-c">in</span> range(len(route) - <span class="num">1</span>):
        <span class="kw-c">for</span> adj_city, dist <span class="kw-c">in</span> road_network[route[k]]:
            <span class="kw-c">if</span> adj_city == route[k + <span class="num">1</span>]:
                total_dist += dist
                <span class="kw-c">break</span>
    <span class="kw">return</span> total_dist

<span class="kw">def</span> <span class="fn">bfs</span>(source, destination):
    frontier = deque([[source]])
    explored = set()
    nodes_explored = <span class="num">0</span>
    max_stored = len(frontier)

    <span class="kw-c">while</span> frontier:
        route = frontier.popleft()
        current_node = route[-<span class="num">1</span>]

        <span class="kw-c">if</span> current_node == destination:
            print(<span class="st">"Path :"</span>, <span class="st">" -&gt; "</span>.join(route))
            print(<span class="st">"Cost :"</span>, calculate_cost(route))
            print(<span class="st">"Nodes Explored (Time Complexity) :"</span>, nodes_explored)
            print(<span class="st">"Max Nodes Stored (Space Complexity) :"</span>, max_stored)
            <span class="kw">return</span>

        <span class="kw-c">if</span> current_node <span class="kw-c">not in</span> explored:
            explored.add(current_node)
            nodes_explored += <span class="num">1</span>

            <span class="kw-c">for</span> adj_city, dist <span class="kw-c">in</span> road_network[current_node]:
                extended_route = route + [adj_city]
                frontier.append(extended_route)

            <span class="kw-c">if</span> len(frontier) &gt; max_stored:
                max_stored = len(frontier)

source = input(<span class="st">"Start City : "</span>)
destination = input(<span class="st">"Goal City : "</span>)

bfs(source, destination)</div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 3 of 7</span>
    </div>
</div>

<!-- ================= PAGE 4 ================= -->
<div class="page">
    <div class="content-body">
        <p><strong>Output :</strong></p>

        <!-- Terminal 1: Ahmedabad -> Chennai -->
        <div class="terminal-card">
            <div class="terminal-tabs">
                <span>Problems</span>
                <span>Output</span>
                <span>Debug Console</span>
                <span class="terminal-tab-active">Terminal</span>
                <span>Ports</span>
            </div>
            <div class="terminal-body"><span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cmd">python .\breadth_first.py</span>
Start City : Ahmedabad
Goal City : Chennai
Path : Ahmedabad -&gt; Indore -&gt; Nagpur -&gt; Hyderabad -&gt; Chennai
Cost : 1975
Nodes Explored (Time Complexity) : 26
Max Nodes Stored (Space Complexity) : 37
<span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cursor">&nbsp;</span></div>
        </div>

        <!-- Terminal 2: Mumbai -> Delhi -->
        <div class="terminal-card">
            <div class="terminal-tabs">
                <span>Problems</span>
                <span>Output</span>
                <span>Debug Console</span>
                <span class="terminal-tab-active">Terminal</span>
                <span>Ports</span>
            </div>
            <div class="terminal-body"><span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cmd">python .\breadth_first.py</span>
Start City : Mumbai
Goal City : Delhi
Path : Mumbai -&gt; Surat -&gt; Vadodara -&gt; Udaipur -&gt; Jaipur -&gt; Delhi
Cost : 1445
Nodes Explored (Time Complexity) : 25
Max Nodes Stored (Space Complexity) : 31
<span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cursor">&nbsp;</span></div>
        </div>

        <h2 class="sec-heading">3. Implement DFS</h2>

        <div class="code-card"><span class="kw">from</span> collections <span class="kw">import</span> deque
<span class="kw">from</span> city_map <span class="kw">import</span> road_network

<span class="kw">def</span> <span class="fn">calculate_cost</span>(route):
    total_dist = <span class="num">0</span>
    <span class="kw-c">for</span> k <span class="kw-c">in</span> range(len(route) - <span class="num">1</span>):
        <span class="kw-c">for</span> adj_city, dist <span class="kw-c">in</span> road_network[route[k]]:
            <span class="kw-c">if</span> adj_city == route[k + <span class="num">1</span>]:
                total_dist += dist
                <span class="kw-c">break</span>
    <span class="kw">return</span> total_dist</div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 4 of 7</span>
    </div>
</div>

<!-- ================= PAGE 5 ================= -->
<div class="page">
    <div class="content-body">
        <div class="code-card"><span class="kw">def</span> <span class="fn">dfs</span>(source, destination):
    frontier = deque([[source]])
    explored = set()
    nodes_explored = <span class="num">0</span>
    max_stored = len(frontier)

    <span class="kw-c">while</span> frontier:
        route = frontier.pop()   <span class="cm"># LIFO stack behavior for Depth-First Search</span>
        current_node = route[-<span class="num">1</span>]

        <span class="kw-c">if</span> current_node == destination:
            print(<span class="st">"Path :"</span>, <span class="st">" -&gt; "</span>.join(route))
            print(<span class="st">"Cost :"</span>, calculate_cost(route))
            print(<span class="st">"Nodes Explored (Time Complexity) :"</span>, nodes_explored)
            print(<span class="st">"Max Nodes Stored (Space Complexity) :"</span>, max_stored)
            <span class="kw">return</span>

        <span class="kw-c">if</span> current_node <span class="kw-c">not in</span> explored:
            explored.add(current_node)
            nodes_explored += <span class="num">1</span>

            <span class="kw-c">for</span> adj_city, dist <span class="kw-c">in</span> road_network[current_node]:
                extended_route = route + [adj_city]
                frontier.append(extended_route)

            <span class="kw-c">if</span> len(frontier) &gt; max_stored:
                max_stored = len(frontier)

source = input(<span class="st">"Start City : "</span>)
destination = input(<span class="st">"Goal City : "</span>)

dfs(source, destination)</div>

        <p>4.</p>
        <p><strong>Output :</strong></p>

        <!-- Terminal 1: Ahmedabad -> Chennai -->
        <div class="terminal-card">
            <div class="terminal-tabs">
                <span>Problems</span>
                <span>Output</span>
                <span>Debug Console</span>
                <span class="terminal-tab-active">Terminal</span>
                <span>Ports</span>
            </div>
            <div class="terminal-body"><span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cmd">python .\depth_first.py</span>
Start City : Ahmedabad
Goal City : Chennai
Path : Ahmedabad -&gt; Indore -&gt; Aurangabad -&gt; Hyderabad -&gt; Visakhapatnam -&gt; Vijayawada -&gt; Chennai
Cost : 2790
Nodes Explored (Time Complexity) : 6
Max Nodes Stored (Space Complexity) : 21
<span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cursor">&nbsp;</span></div>
        </div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 5 of 7</span>
    </div>
</div>

<!-- ================= PAGE 6 ================= -->
<div class="page">
    <div class="content-body">
        <!-- Terminal 2: Mumbai -> Delhi -->
        <div class="terminal-card">
            <div class="terminal-tabs">
                <span>Problems</span>
                <span>Output</span>
                <span>Debug Console</span>
                <span class="terminal-tab-active">Terminal</span>
                <span>Ports</span>
            </div>
            <div class="terminal-body"><span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cmd">python .\depth_first.py</span>
Start City : Mumbai
Goal City : Delhi
Path : Mumbai -&gt; Pune -&gt; Hyderabad -&gt; Visakhapatnam -&gt; Bhubaneswar -&gt; Raipur -&gt; Ranchi -&gt; Kolkata -&gt; Patna -&gt; Varanasi -&gt; Lucknow -&gt; Prayagraj -&gt; Kanpur -&gt; Jhansi -&gt; Bhopal -&gt; Gwalior -&gt; Agra -&gt; Jaipur -&gt; Delhi
Cost : 6425
Nodes Explored (Time Complexity) : 32
Max Nodes Stored (Space Complexity) : 43
<span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cursor">&nbsp;</span></div>
        </div>

        <h2 class="sec-heading">5. A* Search</h2>

        <div class="code-card"><span class="kw">import</span> heapq
<span class="kw">from</span> cities <span class="kw">import</span> graph

<span class="cm"># Straight-line distance / heuristic values</span>
heuristics = {}

<span class="kw">def</span> <span class="fn">a_star</span>(start, goal):
    <span class="cm"># Queue stores tuples of (f_cost, g_cost, path)</span>
    <span class="cm"># f_cost = g_cost + h_cost</span>
    queue = [(<span class="num">0</span>, <span class="num">0</span>, [start])]
    visited = []
    nodes_explored = <span class="num">0</span>
    max_stored = len(queue)

    <span class="kw-c">while</span> queue:
        f_cost, g_cost, path = heapq.heappop(queue)
        city = path[-<span class="num">1</span>]

        <span class="kw-c">if</span> city == goal:
            print(<span class="st">"Path :"</span>, <span class="st">" -&gt; "</span>.join(path))
            print(<span class="st">"Cost :"</span>, find_cost(path))
            print(<span class="st">"Nodes Explored (Time Complexity) :"</span>, nodes_explored)
            print(<span class="st">"Max Nodes Stored (Space Complexity) :"</span>, max_stored)
            <span class="kw">return</span>

        <span class="kw-c">if</span> city <span class="kw-c">not in</span> visited:
            visited.append(city)
            nodes_explored += <span class="num">1</span>

            <span class="kw-c">if</span> city <span class="kw-c">in</span> graph:
                <span class="kw-c">for</span> neighbour, cost <span class="kw-c">in</span> graph[city]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    new_g_cost = g_cost + cost
                    h_cost = heuristics.get(neighbour, <span class="num">0</span>)
                    new_f_cost = new_g_cost + h_cost
                    heapq.heappush(queue, (new_f_cost, new_g_cost, new_path))

            <span class="kw-c">if</span> len(queue) &gt; max_stored:
                max_stored = len(queue)</div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 6 of 7</span>
    </div>
</div>

<!-- ================= PAGE 7 ================= -->
<div class="page">
    <div class="content-body">
        <div class="code-card"><span class="kw">def</span> <span class="fn">find_cost</span>(path):
    total = <span class="num">0</span>
    <span class="kw-c">for</span> i <span class="kw-c">in</span> range(len(path) - <span class="num">1</span>):
        <span class="kw-c">if</span> path[i] <span class="kw-c">in</span> graph:
            <span class="kw-c">for</span> neighbour, cost <span class="kw-c">in</span> graph[path[i]]:
                <span class="kw-c">if</span> neighbour == path[i + <span class="num">1</span>]:
                    total += cost
    <span class="kw">return</span> total

start = input(<span class="st">"Start City : "</span>)
goal = input(<span class="st">"Goal City : "</span>)

a_star(start, goal)</div>

        <p><strong>Output :</strong></p>

        <!-- Terminal 1: Ahmedabad -> Chennai -->
        <div class="terminal-card">
            <div class="terminal-tabs">
                <span>Problems</span>
                <span>Output</span>
                <span>Debug Console</span>
                <span class="terminal-tab-active">Terminal</span>
                <span>Ports</span>
            </div>
            <div class="terminal-body"><span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cmd">python .\astar_search.py</span>
Start City : Ahmedabad
Goal City : Chennai
Path : Ahmedabad -&gt; Vadodara -&gt; Surat -&gt; Mumbai -&gt; Pune -&gt; Hyderabad -&gt; Chennai
Cost : 1890
Nodes Explored (Time Complexity) : 33
Max Nodes Stored (Space Complexity) : 30
<span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cursor">&nbsp;</span></div>
        </div>

        <!-- Terminal 2: Mumbai -> Delhi -->
        <div class="terminal-card">
            <div class="terminal-tabs">
                <span>Problems</span>
                <span>Output</span>
                <span>Debug Console</span>
                <span class="terminal-tab-active">Terminal</span>
                <span>Ports</span>
            </div>
            <div class="terminal-body"><span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cmd">python .\astar_search.py</span>
Start City : Mumbai
Goal City : Delhi
Path : Mumbai -&gt; Surat -&gt; Vadodara -&gt; Udaipur -&gt; Jaipur -&gt; Delhi
Cost : 1445
Nodes Explored (Time Complexity) : 27
Max Nodes Stored (Space Complexity) : 32
<span class="ps-path">PS C:\Users\KHATRI OM KUMAR\Desktop\AI-SUBMITION&gt;</span> <span class="ps-cursor">&nbsp;</span></div>
        </div>
    </div>
    <div class="page-footer">
        <span class="footer-left">KHATRI OM KUMAR | Roll No: 36</span>
        <span class="footer-right">Page 7 of 7</span>
    </div>
</div>

</body>
</html>
"""

html_path = os.path.abspath("om_khatri_lab_report.html")
pdf_path = os.path.abspath("AI_Practical_Submission_Khatri_Om_Kumar.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Wrote {html_path}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if os.path.exists(edge_path):
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Successfully generated PDF: {pdf_path}")
    else:
        print("Edge error:", res.stderr)
else:
    print("Edge not found")
