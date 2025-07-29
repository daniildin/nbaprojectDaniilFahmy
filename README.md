
# Are Superteams Worth It? A Quantitative Analysis of NBA Team Efficiency (2000–2025)

**Authors**: Fahmy Paiziah & Daniil Nasadiuk  
**Duration**: Summer 2025  
**Affiliation**: Independent Study  
**Tools Used**: Python (Pandas, Matplotlib, Seaborn), Jupyter Notebooks  

---

## Executive Summary

In the age of superteams, where franchises stack MVP-caliber talent via trades or free agency, the NBA has seen dramatic shifts in competitive balance and financial strategy. This project explores a fundamental question:

**Are superteams actually worth it financially and competitively compared to balanced teams?**

Using a dataset of team stats, payroll, revenue, and playoff performance from **2000 to 2025**, we built a comprehensive analysis pipeline to:

- Compare **wins, cost per win, revenue per win**
- Label and contrast **superteams** vs **balanced teams**
- Examine **volatility**, ROI, and trends over time
- Visualize results with rich plots for insight and storytelling

---

## Objective

The NBA has evolved from traditional rosters to modern “superteams” constructed around All-Star trios (e.g., LeBron–Wade–Bosh). These teams often dominate media, attract ticket sales, and influence global fanbases, but at what cost?

This project aims to answer:
- Do superteams consistently **outperform balanced teams**?
- Are they **more cost-efficient or just more expensive**?
- Do they offer **higher returns** in terms of revenue per win?
- How **risky or volatile** are they?

---

## Methodology

### Data Sources
- **Advanced team stats** (wins, losses, playoff wins)
- **Payroll data** (inflation-adjusted)
- **Team revenue data**
- Manual labeling of **superteam seasons**

### Superteam Definition
A team is labeled a “superteam” if it satisfies any of the following:
- 2 or more **active All-Stars** on the roster
- 2+ **max contracts** in the same season
- A team popularly regarded as a superteam (e.g., 2017 Warriors)

### Preprocessing
- Cleaned and merged stats by **team + season**
- Standardized team names (e.g., “New Jersey” → “Brooklyn”)
- Converted salaries and revenue to numeric
- Created key metrics:
  - `cost_per_win = payroll / wins`
  - `revenue_per_win = revenue / wins`
  - `win_volatility = std(dev) in wins per team over time`

---

## Core Metrics

We focus on **4 key quantitative comparisons** between superteams and balanced teams:

| Metric             | Superteams       | Balanced Teams     | Interpretation                             |
|--------------------|------------------|---------------------|---------------------------------------------|
| **Avg Wins**       | 47.8             | 40.2                | Superteams win ~8 more games per season     |
| **Cost per Win**   | $2.69M           | $2.50M              | Slightly more expensive, not drastically    |
| **Revenue per Win**| $6.14M           | $5.19M              | Higher ROI for superteams                   |
| **Win Volatility** | 10.95            | 12.15               | Superteams are more consistent              |

These are calculated using groupby-aggregate techniques in Pandas, and validated with t-tests for significance (where applicable).

---

## Visualizations & What They Show

### 1. Violin + Strip Plot — Cost per Win
Combines distribution curves with individual data points to show:
- Median spending for each group
- High-spending outliers (some teams spend >$10M per win!)
- Balanced teams show more **spread**, while superteams cluster tighter

### 2. Scatter Plot — Revenue vs Wins
Used to test correlation between **financial performance** and **sport performance**.
- Balanced teams cluster at lower revenue
- Superteams appear in upper-right quadrants, indicating higher output

### 3. Line Plot — Cost per Win Over Time
Visualizes trends from 2000–2025:
- Both groups show rising costs over time
- Superteams appear to **flatten or drop slightly** post-2020 (possible due to CBA & luxury tax adjustments)

### 4. Box Plot — Cost per Win Spread
Shows range and interquartile range (IQR):
- Balanced teams have wider IQR
- Several outliers with *very high* cost per win appear in both groups

### 5. Bar Chart — Revenue per Win
- Superteams generate higher revenue per win on average
- Supports the claim that **star power sells tickets and merch**

---

## Deep Dive: Boom or Bust?

We explored the **standard deviation** in wins across seasons for each team, then compared those across superteams and balanced teams:

- **Balanced teams** have more boom-or-bust profiles
- Some overperform (e.g., 2004 Pistons), others collapse
- **Superteams** are more predictable, which is valuable for owners

---

## Business & Strategic Implications

| Stakeholder         | Implication |
|---------------------|-------------|
| **Front Office**    | Superteams offer a safer return in wins & revenue, but cost more up front |
| **Investors**       | Revenue per win is higher in superteams, justifying sponsorship & global branding |
| **Fans**            | Superteams create dynasties but reduce league parity |
| **Small Markets**   | Balanced teams can succeed, but face more volatility and need excellent drafting |

---

## Project File Overview

| Notebook                | Description                                               |
|-------------------------|-----------------------------------------------------------|
| `cleaning.ipynb`        | Data cleaning: renaming columns, merging team stats       |
| `calculations.ipynb`    | Group comparisons: average metrics, volatility, ROI       |
| `design.ipynb`          | All visualizations (scatter, violin, box, bar, line plots)|
| `Merged_With_Superteams_And_Metrics.csv` | Final clean dataset with labeled team types |

---

## Limitations & Future Work

- **Revenue Data Gaps**: Some seasons missing complete team revenue info
- **Superteam Labeling**: Subjective to historical perception (manual)
- **External Factors**: Injuries, rule changes, COVID-19 seasons not modeled

**Future Enhancements**:
- Add **playoff wins** and compute **cost per playoff win**
- Include **market size** or fanbase metrics
- Train a **machine learning model** to predict team efficiency based on roster data

---

## Conclusion

Superteams dominate headlines and based on the data, they **also dominate performance and revenue**. While they cost more per win, the return they generate makes them a **stable, high-yield investment**.

Balanced teams, while cheaper, show greater variance. This can lead to surprise playoff runs or total collapses. From a business perspective, **superteams offer better predictability and monetization potential**.

Ultimately, our analysis provides a **data-driven framework** for understanding how financial and strategic decisions translate into on court results and economic returns in the NBA.

After analyzing 25 years of NBA data, we found that superteams do offer measurable advantages: they win more games, generate more revenue per win, and provide greater predictability for team owners and investors. However, they also come with significantly higher financial costs and greater pressure to perform.
In contrast, balanced teams are more cost-efficient but have wider performance variability, capable of both surprise success and total collapse.
Ultimately, superteams are a high-risk, high-reward strategy, best suited for franchises willing to invest heavily in talent for immediate results. As the NBA imposes stricter salary cap rules, the path forward will require smarter, data-driven roster decisions, not just star power.
Answer:
Superteams can be worth it, but only when paired with efficiency, smart contracts, and strong team culture.




---

**End of Report**  
_Last Updated: July 2025_

