# Script to generate the complete index.html with Practice Bank section

html_content = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bernoulli & Binomial Distributions</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link
        href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Lora:ital,wght@0,400;0,600;1,400&family=Outfit:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap"
        rel="stylesheet">
</head>

<body>
    <!-- Custom Cursor -->
    <div id="cursor" class="cursor">∑</div>

    <!-- Loading Screen -->
    <div id="loading-screen">
        <div class="loader-content">
            <div class="spinner"></div>
            <p id="fun-fact">Did you know? Jacob Bernoulli was the first to use the term "integral".</p>
        </div>
    </div>

    <!-- Main Content -->
    <main id="main-content" class="hidden">

        <!-- Hero Section -->
        <section id="hero">
            <div id="falling-signs-container"></div>
            <div class="hero-content">
                <h1>The Art of Probability</h1>
                <p class="subtitle">Exploring Bernoulli & Binomial Distributions</p>
                <button id="explore-btn" class="btn-primary">Start Exploring</button>
            </div>
            <div class="scroll-indicator">
                <span>↓</span>
            </div>
        </section>

        <!-- Jacob Bernoulli Section -->
        <section id="biography">
            <div class="container">
                <div class="bio-grid">
                    <div class="bio-text">
                        <h2>Jacob Bernoulli</h2>
                        <div class="info-box">
                            <p class="bio-intro">A Swiss mathematician who changed how we understand chance.</p>
                            <p>Jacob Bernoulli (1654–1705) was one of the many prominent mathematicians in the Bernoulli
                                family. His most significant work, <em>Ars Conjectandi</em> (The Art of Conjecturing),
                                was published posthumously and established the fundamental principles of probability
                                theory.</p>
                            <div class="fun-fact-card">
                                <h3>Fun Fact</h3>
                                <p>He was so fascinated by the logarithmic spiral that he asked for one to be engraved
                                    on his tombstone with the phrase <em>"Eadem mutata resurgo"</em> ("I shall arise the
                                    same, though changed").</p>
                            </div>
                        </div>
                    </div>
                    <div class="bio-image-wrapper">
                        <img src="assets/bernoulli.png" alt="Portrait of Jacob Bernoulli" class="bio-image">
                        <div class="image-frame"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Importance Section -->
        <section id="importance">
            <div class="container">
                <h2>Why Study Bernoulli & Binomial Distributions?</h2>
                <div class="importance-content info-box">
                    <p>Understanding Bernoulli and Binomial distributions is fundamental to mastering probability and
                        statistics. They are the building blocks for more complex concepts like the Normal Distribution
                        (via the Central Limit Theorem) and Poisson Distribution.</p>
                    <p>From predicting election outcomes to analyzing medical trial results and quality assurance in
                        manufacturing, these tools allow us to quantify uncertainty and make informed decisions in a
                        world full of randomness.</p>
                </div>
            </div>
        </section>

        <!-- Theory Section -->
        <section id="theory">
            <div class="container">
                <h2>Understanding the Math</h2>

                <div class="theory-grid">
                    <!-- Bernoulli Distribution -->
                    <div class="theory-card">
                        <h3>Bernoulli Distribution</h3>
                        <p class="definition">The probability distribution of a random variable which takes the value 1
                            with probability <em>p</em> and the value 0 with probability <em>q = 1 - p</em>.</p>
                        <div class="formula-box">
                            P(X = k) = p<sup>k</sup>(1-p)<sup>1-k</sup>
                        </div>
                        <p class="formula-explanation">For k ∈ {0, 1}</p>
                        <ul class="applications-list">
                            <li>Coin Toss (Heads/Tails)</li>
                            <li>Success/Failure of a medical treatment</li>
                            <li>Pass/Fail in an exam</li>
                            <li>Yes/No survey responses</li>
                        </ul>
                    </div>

                    <!-- Binomial Distribution -->
                    <div class="theory-card">
                        <h3>Binomial Distribution</h3>
                        <p class="definition">The discrete probability distribution of the number of successes in a
                            sequence of <em>n</em> independent experiments, each asking a yes–no question.</p>
                        <div class="formula-box">
                            P(X = k) = C(n,k) p<sup>k</sup>(1-p)<sup>n-k</sup>
                        </div>
                        <p class="formula-explanation">Where C(n,k) is the binomial coefficient.</p>
                        <ul class="applications-list">
                            <li>Number of heads in 10 coin tosses</li>
                            <li>Defective items in a production batch</li>
                            <li>Number of spam emails in a folder</li>
                            <li>Voter preference in a sample group</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Real-World Applications Section -->
        <section id="applications">
            <div class="container">
                <h2>Real-World Applications</h2>
                <div class="applications-grid">
                    <div class="app-card">
                        <div class="app-icon">💊</div>
                        <h3>Medical Trials</h3>
                        <p>Determining the success rate of a new drug. Each patient represents a Bernoulli trial
                            (Cured/Not Cured), and the total number of cured patients follows a Binomial distribution.
                        </p>
                    </div>
                    <div class="app-card">
                        <div class="app-icon">🏭</div>
                        <h3>Quality Control</h3>
                        <p>Testing a batch of manufactured products. Each item is either defective or functional.
                            Manufacturers use this to estimate the probability of a bad batch.</p>
                    </div>
                    <div class="app-card">
                        <div class="app-icon">🗳️</div>
                        <h3>Election Polling</h3>
                        <p>Predicting election results based on a sample. Each voter's choice (Candidate A vs. B) is a
                            trial, helping analysts estimate the overall population's preference.</p>
                    </div>
                    <div class="app-card">
                        <div class="app-icon">🏀</div>
                        <h3>Sports Analytics</h3>
                        <p>Analyzing a player's free throw performance. Each shot is a success or failure. Coaches use
                            this data to predict future performance and strategy.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Interactive Visualization Section -->
        <section id="visualization">
            <div class="container">
                <h2>Interactive Lab</h2>
                <p class="viz-subtitle">Experiment with the parameters to see how the distribution changes.</p>

                <div class="viz-layout">
                    <div class="controls-panel">
                        <h3>Controls</h3>

                        <div class="control-group">
                            <label for="prob-p">Probability of Success (p): <span id="p-value">0.5</span></label>
                            <input type="range" id="prob-p" min="0" max="1" step="0.01" value="0.5">
                        </div>

                        <div class="control-group">
                            <label for="trials-n">Number of Trials (n): <span id="n-value">10</span></label>
                            <input type="range" id="trials-n" min="1" max="50" step="1" value="10">
                        </div>

                        <div class="stats-panel">
                            <div class="stat-item">
                                <span class="stat-label">Mean (μ):</span>
                                <span id="stat-mean" class="stat-value">5.00</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-label">Variance (σ²):</span>
                                <span id="stat-var" class="stat-value">2.50</span>
                            </div>
                        </div>
                    </div>

                    <div class="chart-container">
                        <canvas id="distributionChart"></canvas>
                    </div>
                </div>
            </div>
        </section>

'''

# Write to file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
    
print("Part 1 written successfully!")
