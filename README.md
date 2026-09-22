# AI-SUBMITION

Artificial Intelligence Practical Lab Submissions & Experiments by Khatri Om Kumar (Roll No: 36, BE-III CSE, MSU Baroda).

---

## 📌 Contents

### 1. Search Algorithms (Indian City Map - Practicals 1, 2, 3)
- **15 Random Initial & Final States (`random_states.py`)** - Curated and reproducible 15 initial and goal city pairs across India.
- **Breadth-First Search (`breadth_first.py`)** - Uninformed search exploring level by level; evaluates all 15 state pairs.
- **Depth-First Search (`depth_first.py`)** - Explores deep branches before backtracking; evaluates all 15 state pairs.
- **A* Search (`astar_search.py`)** - Informed heuristic search using straight-line (great-circle) distance to goal as an admissible heuristic $h(n)$; evaluates all 15 state pairs.
- **Search Benchmark Runner (`run_all_search_15.py`)** - Runs BFS, DFS, and A* side-by-side across all 15 cases and displays a full comparative observation table.
- **City Map & Coordinates (`city_map.py`, `cities.py`)** - Graph representation and latitude/longitude coordinates for straight-line distance calculation.

### 2. Hill Climbing Algorithms (8-Queens Problem)
- **Steepest-Ascent Hill Climbing (`steepest_hill.py`)**
- **First-Choice Hill Climbing (`first_choice_hc.py`)**
- **Stochastic Hill Climbing (`stochastic_hc.py`)**
- **Random-Restart Hill Climbing (`restart_hill.py`)**
- **Utilities & Experiment Benchmarks (`nqueens_utils.py`, `queens_common.py`, `run_experiments.py`)**

### 3. Reports & Documentation
- **`AI_PRACTICLE_SUBMITTION_KHATRI_OM_KUMAR.PDF`** - Complete 26-page laboratory practical report containing source code, authentic terminal screenshot cards for all 15 runs, comparative observation tables, and analytical viva answers.
- **`complete_lab_submission.html`** - Responsive HTML document for the PDF report.
- **`generate_complete_submission.py`** - Headless automated PDF compilation script via Microsoft Edge.

---

## 🚀 Usage

### Run Search Algorithms (15 Test Cases):
```bash
# View the 15 Random Initial & Final States
python random_states.py

# Run BFS across all 15 cases
python breadth_first.py

# Run DFS across all 15 cases
python depth_first.py

# Run A* Search across all 15 cases
python astar_search.py

# Run the 15-case comparative benchmark
python run_all_search_15.py
```

### Run Hill Climbing Experiments:
```bash
python run_experiments.py
```

### Recompile the Submission PDF:
```bash
python generate_complete_submission.py
```