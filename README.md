# Median of Data Stream Visualizer

An interactive Streamlit application that visualizes how the median of a data stream changes as new numbers are inserted.

## Features

- Interactive number insertion
- Real-time median calculation
- Max Heap visualization
- Min Heap visualization
- Running data stream display

## Tech Stack

- Python
- Streamlit
- Heapq
- Graphviz

## How It Works

The application maintains two heaps:

- Max Heap stores the smaller half of the numbers.
- Min Heap stores the larger half.

After each insertion:

1. The heaps are balanced.
2. The median is calculated.
3. Both heap structures are updated visually.

This allows median retrieval in **O(1)** while insertion takes **O(log n)**.

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/median-stream-visualizer.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## Example

Input Stream

```
5 2 10 7 1
```

Median after each insertion

```
5
3.5
5
6
5
```

## Learning Outcomes

- Heap Data Structure
- Priority Queue
- Median of Data Stream Algorithm
- Streamlit UI Development
- Graph Visualization

## Future Improvements

- Delete elements from stream
- Support duplicate highlighting
- Time complexity visualization
- Animation for heap balancing