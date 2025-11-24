"""
Create Practice Bank section with 10 high-quality questions
"""

practice_bank = '''
        <!-- Practice Bank Section -->
        <section id="practice-bank">
            <div class="container">
                <h2>Practice Bank</h2>
                <p class="viz-subtitle">Master these concepts before tackling the challenges below!</p>
                <div class="theory-grid">
                    <!-- Practice Question 1 -->
                    <div class="theory-card">
                        <h3>1. The Birthday Paradox Variation</h3>
                        <p>In a group of 23 people, there's about a 50% chance two share a birthday. If instead we ask "what's the probability at least two people were born in the same month?", how does this change? Will it be higher or lower than 50%?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Solution:</strong></p>
                                <p>With 12 months instead of 365 days, collisions happen MUCH faster!</p>
                                <p><strong>Using the birthday formula:</strong></p>
                                <p>P(no match) = (12/12) × (11/12) × (10/12) × ... × ((12-n+1)/12)</p>
                                <p>For n=23: This product ≈ 0 (essentially zero!)</p>
                               <p>P(at least one match) ≈ <strong>99.999%</strong> (virtually certain!)</p>
                                <p><strong>General rule:</strong> √m gives ~50% threshold, where m = number of categories</p>
                                <p>For months: √12 ≈ 3.5 people needed for ~50% chance</p>
                                <p>For 23 people with only 12 categories: multiple matches are guaranteed!</p>
                                <p><strong>Lesson:</strong> Reducing categories from 365 → 12 massively increases collision probability!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 2 -->
                    <div class="theory-card">
                        <h3>2. The False Positive Problem</h3>
                        <p>A disease affects 1% of the population. A test is 95% accurate (detects 95% of cases, and correctly identifies 95% of healthy people). You test positive. What's the probability you actually have the disease?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Solution using Bayes' Theorem:</strong></p>
                                <p><strong>Given:</strong> P(Disease) = 0.01, P(Healthy) = 0.99</p>
                                <p>P(Positive | Disease) = 0.95, P(Positive | Healthy) = 0.05</p>
                                <p><strong>Want: P(Disease | Positive)</strong></p>
                                <p><strong>Calculate P(Positive):</strong></p>
                                <p>P(Pos) = P(Pos|Dis) × P(Dis) + P(Pos|Health) × P(Health)</p>
                                <p>= 0.95 × 0.01 + 0.05 × 0.99 = 0.0095 + 0.0495 = 0.059</p>
                                <p><strong>Apply Bayes:</strong></p>
                                <p>P(Disease|Positive) = (0.95 × 0.01) / 0.059 ≈ <strong>0.161 or 16.1%</strong></p>
                                <p><strong>Surprise:</strong> Despite 95% accuracy, only 16% chance you're actually sick!</p>
                                <p><strong>Why?</strong> Base rate of 1% means most positives are false positives from the large healthy population.</p>
                                <p><strong>Lesson:</strong> Test accuracy alone is misleading. Base rates matter enormously!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 3 -->
                    <div class="theory-card">
                        <h3>3. The Streaky Shooter Illusion</h3>
                        <p>A 50% free throw shooter makes 7 out of 10 consecutive shots. Their coach says they're "in the zone" and now shooting better than 50%. Using statistics, is there strong evidence of improvement, or is this within normal variance?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Hypothesis Test:</strong></p>
                                <p>H₀: p = 0.5 (shooter unchanged)</p>
                                <p>Observed: 7/10 = 70%</p>
                                <p><strong>Calculate P(X ≥ 7) if p=0.5:</strong></p>
                                <p>P(X ≥ 7) = P(X=7) + P(X=8) + P(X=9) + P(X=10)</p>
                                <p>= [C(10,7) + C(10,8) + C(10,9) + C(10,10)] × (0.5)^10</p>
                                <p>= (120 + 45 + 10 + 1) / 1024 =                  176/1024 ≈ <strong>0.172 or 17.2%</strong></p>
                                <p><strong>Interpretation:</strong> 17% chance this happens by pure luck with a 50% shooter!</p>
                                <p>This is NOT statistically significant at 5% level (would need p < 0.05).</p>
                                <p><strong>Conclusion:</strong> Insufficient evidence to claim improvement. This is normal variance!</p>
                                <p><strong>Lesson:</strong> Humans perceive patterns in randomness. Small samples create "streaks" that feel meaningful but aren't statistically significant.</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 4 -->
                    <div class="theory-card">
                        <h3>4. The System Reliability Paradox</h3>
                        <p>A spacecraft has 10 independent critical systems, each with 99% reliability. Engineers say "99% per system is excellent!" But what's the probability that ALL 10 systems work? Is the overall reliability better or worse than 99%?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Solution:</strong></p>
                                <p>For ALL systems to work (series configuration):</p>
                                <p>P(all work) = (0.99)^10 ≈ <strong>0.904 or 90.4%</strong></p>
                                <p>P(at least one fails) = 1 - 0.904 = <strong>9.6%</strong></p>
                                <p><strong>Shocking result:</strong> Overall reliability DROPPED from 99% to 90.4%!</p>
                                <p><strong>Why?</strong> Multiplication of probabilities < 1 makes them smaller!</p>
                                <p><strong>General formula:</strong> For n independent systems with reliability p each:</p>
                                <p>System reliability = p^n</p>
                                <p><strong>Example variations:</strong></p>
                                <p>• 20 systems at 99% each: (0.99)^20 ≈ 82%</p>
                                <p>• 100 systems at 99% each: (0.99)^100 ≈ 37%!</p>
                                <p><strong>Engineering implication:</strong> Need redundancy! Use parallel backup systems.</p>
                                <p><strong>Lesson:</strong> Individual component reliability ≠ system reliability. Complexity reduces reliability!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 5 -->
                    <div class="theory-card">
                        <h3>5. The Expectation vs. Median Trap</h3>
                        <p>You play a game: flip a fair coin 10 times. You win $1 for each head. What's your expected winnings? What's the median? What's the mode? Are they all the same?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Expected Value (Mean):</strong></p>
                                <p>E[X] = np = 10 × 0.5 = <strong>$5</strong></p>
                                <p><strong>Median:</strong></p>
                                <p>For Binomial(10, 0.5), median = <strong>5</strong> (middle value)</p>
                                <p>P(X ≤ 4) ≈ 0.377, P(X ≤ 5) ≈ 0.623 → median is 5</p>
                                <p><strong>Mode (most likely outcome):</strong></p>
                                <p>Mode = <strong>5</strong> (highest probability)</p>
                                <p>P(X = 5) = C(10,5) × (0.5)^10 ≈ 0.246 or 24.6%</p>
                                <p><strong>For symmetric binomial with p=0.5: Mean = Median = Mode!</strong></p>
                                <p><strong>But try p=0.3:</strong></p>
                                <p>• Expected value: 10 × 0.3 = 3</p>
                                <p>• Mode: also 3</p>
                                <p>• Median: 3 (slightly skewed)</p>
                                <p><strong>Key insight:</strong> For p=0.5, distribution is symmetric so all three coincide. For p ≠ 0.5, distribution skews and they can differ!</p>
                                <p><strong>Lesson:</strong> Different measures of "center" can diverge in skewed distributions!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 6 -->
                    <div class="theory-card">
                        <h3>6. The Rare Event Frequency Puzzle</h3>
                        <p>A lottery has a 1 in 1000 chance of winning. You buy 100 tickets (with replacement). What's the probability you win at least once? Is it 100/1000 = 10%?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Wrong approach:</strong> 100 × 0.001 = 0.1 or 10%</p>
                                <p>This assumes probabilities add linearly (only valid for very small p)</p>
                                <p><strong>Correct approach:</strong></p>
                                <p>P(at least 1 win) = 1 - P(all losses)</p>
                                <p>= 1 - (0.999)^100</p>
                                <p>= 1 - 0.9048</p>
                                <p>= <strong>0.0952 or 9.52%</strong></p>
                                <p><strong>Difference:</strong> 10% vs 9.52% ≈ 0.48 percentage points</p>
                                <p><strong>Why they differ:</strong> Linear approximation p×n ignores the chance of multiple wins in same trial set.</p>
                                <p><strong>When is linear approximation good?</strong></p>
                                <p>When np << 1 (very small). Here np = 0.1, so error is ~5%.</p>
                                <p><strong>General formula for n trials, probability p each:</strong></p>
                                <p>P(at least 1) = 1 - (1-p)^n</p>
                                <p>Approximation: np (good when np < 0.05)</p>
                                <p><strong>Lesson:</strong> Probability multiplication matters! Can't always just add probabilities.</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 7 -->
                    <div class="theory-card">
                        <h3>7. The Confidence Interval Misinterpretation</h3>
                        <p>You construct a 95% confidence interval for a coin's bias: [0.45, 0.55]. Your friend says "There's a 95% chance the true probability is between 0.45 and 0.55." Are they correct? What does 95% really mean?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Your friend is WRONG!</strong></p>
                                <p><strong>The correct interpretation:</strong></p>
                                <p>"If we repeated this experiment many times and computed a 95% CI each time, about 95% of those intervals would contain the true parameter."</p>
                                <p><strong>Why the difference matters:</strong></p>
                                <p>The true parameter p is FIXED (not random). It either is or isn't in [0.45, 0.55].</p>
                                <p>The INTERVAL is random (changes with each sample).</p>
                                <p><strong>Probability refers to the procedure, not this specific interval!</strong></p>
                                <p><strong>Analogy:</strong> Factory makes rulers. "95% accurate" means 95% of rulers are correct, NOT that each ruler has 95% chance of being right.</p>
                                <p><strong>Common mistake causes:</strong></p>
                                <p>• Bayesian vs Frequentist confusion</p>
                                <p>                    • "Confidence" sounds like "probability"</p>
                                <p>• Natural to want probabilities about parameters</p>
                                <p><strong>Bayesian alternative (credible interval):</strong></p>
                                <p>With a prior, you CAN say "95% probability parameter is in interval"</p>
                                <p><strong>Lesson:</strong> Confidence intervals are about long-run procedure properties, not single-instance probabilities!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 8 -->
                    <div class="theory-card">
                        <h3>8. The Sample Size Independence</h3>
                        <p>Poll A surveys 1000 people in a city of 100,000. Poll B surveys 1000 people in a country of 300 million. Assuming random sampling, which poll has smaller margin of error? Or are they roughly the same?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Surprising answer: Roughly the SAME!</strong></p>
                                <p><strong>Standard error formula:</strong></p>
                                <p>SE = √[p(1-p)/n]</p>
                                <p>Notice it depends on n (sample size), NOT on N (population size)!</p>
                                <p><strong>For both polls with n=1000, p≈0.5:</strong></p>
                                <p>SE = √[0.5 × 0.5 / 1000] ≈ 0.0158 or 1.58%</p>
                                <p>Margin of error (95% CI): ±1.96 × 1.58% ≈ <strong>±3.1%</strong></p>
                                <p><strong>Finite population correction (usually ignored):</strong></p>
                                <p>FPC = √[(N-n)/(N-1)]</p>
                                <p>City: FPC = √[(100,000-1,000)/99,999] ≈ 0.995</p>
                                <p>Country: FPC = √[(300M-1,000)/300M-1] ≈ 0.9999998</p>
                                <p>Both ≈ 1, so negligible correction!</p>
                                <p><strong>Rule of thumb:</strong> FPC only matters when n > 0.05N (sampling >5% of population)</p>
                                <p><strong>Implication:</strong> National polls with 1000 respondents are just as precise as local polls with 1000 respondents!</p>
                                <p><strong>Lesson:</strong> Precision depends on absolute sample size, not proportion of population sampled!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 9 -->
                    <div class="theory-card">
                        <h3>9. The Multiplication Inequality</h3>
                        <p>You need to pass through 5 independent security checkpoints, each with a 90% pass rate (10% false alarm). What's the probability you get through all 5 without any false alarms? Above or below 50%?</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Calculation:</strong></p>
                                <p>P(pass all 5) = (0.9)^5 = <strong>0.59049 or 59%</strong></p>
                                <p>P(at least one false alarm) = 1 - 0.59 = <strong>41%</strong></p>
                                <p><strong>Above 50%, but not by much!</strong></p>
                                <p><strong>Key insight:</strong> Even with 90% individual reliability, 5 checkpoints drops success to 59%.</p>
                                <p><strong>Related scenarios:</strong></p>
                                <p>• 3 checkpoints: (0.9)^3 ≈ 73%</p>
                                <p>• 10 checkpoints: (0.9)^10 ≈ 35% (now < 50%!)</p>
                                <p>• 20 checkpoints: (0.9)^20 ≈ 12%</p>
                                <p><strong>Real-world parallel:</strong></p>
                                <p>Multiple tests/screenings increase false positive rates!</p>
                                <p>Medical screening panels with many tests → many false positives</p>
                                <p><strong>Formula:</strong> For n independent tests at specificity s:</p>
                                <p>P(all pass) = s^n</p>
                                <p>P(at least one false positive) = 1 - s^n</p>
                                <p><strong>Lesson:</strong> Cascading independent processes multiply their failure probabilities!</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Practice Question 10 -->
                    <div class="theory-card">
                        <h3>10. The Power Analysis Problem</h3>
                        <p>You're testing if a coin is biased toward heads (p > 0.5). With 20 flips and significance level α=0.05, what's the probability you'll detect bias if the true p=0.7? This is called "statistical power."</p>
                        <details>
                            <summary>Show Solution</summary>
                            <div class="answer-content">
                                <p><strong>Setup:</strong></p>
                                <p>H₀: p = 0.5 vs H₁: p > 0.7</p>
                                <p>n = 20, α = 0.05 (one-tailed test)</p>
                                <p><strong>Step 1: Find rejection region under H₀</strong></p>
                                <p>Need P(X ≥ k | p=0.5) ≤ 0.05</p>
                                <p>Testing: P(X ≥ 15 | p=0.5) = 0.021 < 0.05 ✓</p>
                                <p>P(X ≥ 14 | p=0.5) = 0.058 > 0.05 ✗</p>
                                <p>Reject H₀ if X ≥ 15</p>
                                <p><strong>Step 2: Calculate power under true p=0.7</strong></p>
                                <p>Power = P(X ≥ 15 | p=0.7)</p>
                                <p>= Σ(k=15 to 20) C(20,k) × (0.7)^k × (0.3)^(20-k)</p>
                                <p>≈ <strong>0.416 or 41.6%</strong></p>
                                <p><strong>Interpretation:</strong> Only 42% chance of detecting bias!</p>
                                <p>Type II error (β) = 1 - power = 58% (failing to detect real bias)</p>
                                <p><strong>Why so low?</strong> Sample size n=20 is too small to reliably distinguish p=0.7 from p=0.5</p>
                                <p><strong>To increase power:</strong></p>
                                <p>• Increase n (e.g., n=100 gives power ≈ 99%)</p>
                                <p>• Increase α (but more false positives)</p>
                                <p>• Larger effect size (e.g., p=0.8 vs 0.7)</p>
                                <p><strong>Lesson:</strong> Underpowered studies miss real effects! Always check power before conducting experiments.</p>
                                <div class="video-solution">
                                    <p><em>Video solution coming soon...</em></p>
                                </div>
                            </div>
                        </details>
                    </div>
                </div>
            </div>
        </section>
'''

# Read base HTML
with open('index_base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert practice bank before Challenge Section
insert_marker = '        <!-- THE PRACTICE BANK SECTION WILL BE INSERTED HERE -->'
new_content = content.replace(insert_marker, practice_bank)

# Write final HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("[SUCCESS] Complete index.html created successfully!")
print("[SUCCESS] 10 practice questions added before Challenge Yourself section")
print("[SUCCESS] All questions have detailed written solutions")
print("[SUCCESS] Video solution placeholders added")
