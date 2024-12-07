<body>
  <h1>CSCE2303 – Computer Organization and Assembly Language Programming</h1>
  <h2>Fall 2024 - Project 2: Memory Hierarchy Simulator</h2>
  
  <h3>Project Overview</h3>
  <p>
    The goal of this project is to implement a simple simulator for the memory caching system. 
    This document details the requirements of the simulator.
  </p>
  
  <h3>Implementation Language</h3>
  <p>
    Any general-purpose programming language. The resulting application can either be a 
    console application or a graphical user interface (GUI) application (desktop, web-based, or mobile app) as a bonus feature.
  </p>
  
  <h3>Team Size</h3>
  <p>2 or 3 students</p>
  
  <h3>The Memory Hierarchy</h3>
  <p>
    The basic requirements for the project assume a simplified read-only one-level caching 
    system that uses direct mapping. The underlying memory address space is assumed to be a 
    byte-addressable memory.
  </p>
  
  <h3>Simulator Inputs</h3>
  <ol>
    <li>
      <b>Memory Information:</b> 
      <ul>
        <li>The number of bits needed to address the memory (an integer between 16 and 40).</li>
        <li>The memory access time in cycles (an integer between 50 and 200).</li>
      </ul>
    </li>
    <li>
      <b>Cache Information:</b> 
      <ul>
        <li>The total cache size S (in bytes).</li>
        <li>The cache line size L (in bytes).</li>
        <li>The number of cycles needed to access the cache (an integer between 1 and 10 clock cycles).</li>
      </ul>
    </li>
    <li>
      <b>Access Sequence:</b> 
      <ul>
        <li>A sequence of memory addresses accessed by a program, given in bytes.</li>
        <li>This sequence should be provided as a text file containing a comma-separated list of byte addresses.</li>
      </ul>
    </li>
  </ol>
  
  <h3>Simulation and Simulation Outputs</h3>
  <p>The simulator should:</p>
  <ul>
    <li>Trace the cache behavior for the input sequence of memory accesses.</li>
    <li>Keep track of valid bits, tags, and cache content after each access.</li>
    <li>Track the total number of accesses, hits, and misses.</li>
  </ul>
  
  <p>After each memory access, output the following:</p>
  <ul>
    <li>The index and tag referred to by this access.</li>
    <li>Whether this access is a hit or a miss.</li>
    <li>Total number of hits, misses, and accesses so far.</li>
  </ul>
  
  <p>At the end of the sequence, output:</p>
  <ul>
    <li>Valid bits and tags of all entries.</li>
    <li>The hit and miss ratios.</li>
    <li>The Average Memory Access Time (AMAT) of the memory hierarchy (in cycles).</li>
  </ul>
  
  <h3>Bonus Features</h3>
  <p>To earn bonus marks, implement up to two of the following features:</p>
  <ol>
    <li>Building the application as a GUI application (desktop, web-based, or mobile app).</li>
    <li>Supporting set and full associativity, with user-specified associativity levels.</li>
    <li>Supporting multi-level cache hierarchies, where the user specifies the number of levels and parameters for each.</li>
    <li>Supporting separate caches for instructions and data, with two access sequences.</li>
    <li>Supporting a read-write cache with user-specified writing policies and labeled access sequences.</li>
  </ol>
  
  <h3>General Guidelines</h3>
  <ul>
    <li>Each group member must log their activities in a journal file.</li>
    <li>Submit a single compressed folder containing:
      <ul>
        <li>A journal folder with each team member's journal.</li>
        <li>A source code folder with the simulator code.</li>
        <li>A test folder with all input files (sequence files) used for testing.</li>
        <li>A PDF report with:
          <ul>
            <li>Students’ names and IDs.</li>
            <li>A brief description of the implementation and bonus features.</li>
            <li>Design decisions and assumptions made.</li>
            <li>Known bugs or issues in the simulator.</li>
            <li>A user guide with instructions and examples (with screenshots).</li>
            <li>Sequences simulated and their outputs.</li>
            <li>Optional: A section about your project experience (not graded).</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  
  <h3>Important Notes</h3>
  <ul>
    <li>Write all code from scratch. Plagiarized submissions will receive a grade of zero and be reported.</li>
    <li>Examples of unacceptable sources: Other teams, previous course offerings, open-source software, tutors, or online code.</li>
  </ul>
  
  <h3>Deadline</h3>
  <p>Submit the project by <b>Thursday, Dec 5, 2024 (11:59 pm)</b>. Demos will be scheduled on <b>Sunday, Dec 8</b> and <b>Monday, Dec 9</b>.</p>
  
  <h3>Grading Criteria</h3>
  <ul>
    <li>Project 2 accounts for 15% of the course marks.</li>
    <li>Bonus: Each feature is worth 5% (up to 2 features, max 10%).</li>
    <li>Deductions:
      <ul>
        <li>-5% for incorrect directory structure.</li>
        <li>-5% per day for late submission (max 2 days).</li>
        <li>-100% for plagiarized submissions.</li>
      </ul>
    </li>
    <li>Group members may receive different grades based on their contributions.</li>
  </ul>
</body>
</html>
