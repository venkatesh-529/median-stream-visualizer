import streamlit as st
import heapq
import graphviz

st.set_page_config(page_title="Median Data Stream Visualizer", layout="wide")

# App title
st.title("📈 Median of Data Stream Visualizer with Heap Trees")

# Session state initialization
if 'maxHeap' not in st.session_state:
    st.session_state.maxHeap = []  # max-heap (store negatives)
if 'minHeap' not in st.session_state:
    st.session_state.minHeap = []  # min-heap
if 'stream' not in st.session_state:
    st.session_state.stream = []

# Function to add a number with proper heap balancing
def add_number(num):
    # If no elements yet, just add to maxHeap
    if not st.session_state.maxHeap and not st.session_state.minHeap:
        heapq.heappush(st.session_state.maxHeap, -num)
    else:
        median = get_median()
        # If heaps are equal size
        if len(st.session_state.maxHeap) == len(st.session_state.minHeap):
            if num > median:
                heapq.heappush(st.session_state.minHeap, num)
            else:
                heapq.heappush(st.session_state.maxHeap, -num)
        # If maxHeap has more elements
        elif len(st.session_state.maxHeap) > len(st.session_state.minHeap):
            if num < median:
                heapq.heappush(st.session_state.maxHeap, -num)
                # Rebalance
                heapq.heappush(st.session_state.minHeap, -heapq.heappop(st.session_state.maxHeap))
            else:
                heapq.heappush(st.session_state.minHeap, num)
        # If minHeap has more elements
        else:
            if num > median:
                heapq.heappush(st.session_state.minHeap, num)
                # Rebalance
                heapq.heappush(st.session_state.maxHeap, -heapq.heappop(st.session_state.minHeap))
            else:
                heapq.heappush(st.session_state.maxHeap, -num)

    st.session_state.stream.append(num)

# Function to get current median
def get_median():
    if len(st.session_state.maxHeap) > len(st.session_state.minHeap):
        return float(-st.session_state.maxHeap[0])
    return (-st.session_state.maxHeap[0] + st.session_state.minHeap[0]) / 2

# Tree visualization using Graphviz
def draw_heap_graph(heap, name="Heap"):
    dot = graphviz.Digraph()
    n = len(heap)
    for i in range(n):
        label = str(-heap[i]) if name == "MaxHeap" else str(heap[i])
        dot.node(str(i), label)
        if 2*i+1 < n:
            dot.edge(str(i), str(2*i+1))
        if 2*i+2 < n:
            dot.edge(str(i), str(2*i+2))
    return dot

# Sidebar input
with st.sidebar:
    st.header("➕ Add a Number")
    new_num = st.number_input("Enter a number to add", step=1)
    if st.button("Add Number"):
        add_number(int(new_num))

    if st.button("Clear Stream"):
        st.session_state.maxHeap.clear()
        st.session_state.minHeap.clear()
        st.session_state.stream.clear()

# Display current median
if st.session_state.stream:
    st.metric("📍 Current Median", get_median())

# Display stream as a bar chart
with st.expander("📊 Stream Chart"):
    st.bar_chart(st.session_state.stream)

# Display heaps and trees
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔺 Max Heap (Left Half)")
    st.write("Raw:", [-x for x in st.session_state.maxHeap])
    max_tree = draw_heap_graph(st.session_state.maxHeap, "MaxHeap")
    st.graphviz_chart(max_tree)

with col2:
    st.subheader("🔻 Min Heap (Right Half)")
    st.write("Raw:", st.session_state.minHeap)
    min_tree = draw_heap_graph(st.session_state.minHeap, "MinHeap")
    st.graphviz_chart(min_tree)


