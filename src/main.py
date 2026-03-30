import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
from datetime import datetime

# Add parent directory to path to import model
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.model import predict_addiction

# Page configuration
st.set_page_config(
    page_title="MindTrack AI",
    page_icon=":brain:",
    layout="wide"
)

st.title("MindTrack AI - Digital Addiction Analyzer")
st.markdown("---")

# Input section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Digital Usage")
    screen_time = st.slider("Screen Time (hours/day)", 0.0, 15.0, 5.0, 
                            help="Total time on phone, laptop, TV")
    social_media = st.slider("Social Media Hours (hours/day)", 0.0, 10.0, 2.0,
                            help="Instagram, Facebook, TikTok, etc.")
    gaming_hours = st.slider("Gaming Hours (hours/day)", 0.0, 8.0, 1.0,
                            help="Time spent on video games")
    
with col2:
    st.subheader("Health & Productivity")
    sleep = st.slider("Sleep Hours (hours/night)", 0.0, 12.0, 7.0,
                     help="Average sleep duration")
    study = st.slider("Study/Work Hours (hours/day)", 0.0, 12.0, 4.0,
                     help="Productive work or study time")
    physical_activity = st.slider("Physical Activity (hours/day)", 0.0, 5.0, 1.0,
                                  help="Exercise, sports, walking")
    family_time = st.slider("Family/Social Time (hours/day)", 0.0, 8.0, 2.0,
                           help="Time with family or friends in person")

st.markdown("---")

def calculate_score(screen_time, social_media, sleep, study, gaming_hours, physical_activity, family_time):
    negative_score = (screen_time * 8) + (social_media * 12) + (gaming_hours * 7)
    positive_score = (sleep * 6) + (study * 9) + (physical_activity * 5) + (family_time * 4)
    score = negative_score - positive_score + 50
    return max(0, min(100, score))

def get_risk_level(score):
    if score >= 65:
        return "HIGH", "red", "Severe digital dependency detected. Immediate action required."
    elif score >= 35:
        return "MEDIUM", "orange", "Unhealthy patterns developing. Time to make changes."
    else:
        return "LOW", "green", "Healthy digital habits. Keep maintaining this balance."

def get_detailed_insights(screen_time, social_media, sleep, study, gaming_hours, physical_activity, family_time, score):
    insights = {
        "critical": [],
        "warnings": [],
        "positive": [],
        "tips": []
    }
    
    # Screen time analysis
    if screen_time > 8:
        insights["critical"].append(f"CRITICAL: {screen_time}h screen time is extremely high (healthy: less than 4h)")
        insights["tips"].append("Use app timers to limit screen time to 4 hours maximum")
    elif screen_time > 6:
        insights["warnings"].append(f"WARNING: {screen_time}h screen time is high")
        insights["tips"].append("Try reducing screen time by 30 minutes each week")
    elif screen_time > 4:
        insights["warnings"].append(f"NOTICE: {screen_time}h screen time is moderate")
    else:
        insights["positive"].append(f"GOOD: {screen_time}h screen time is within healthy range")
    
    # Social media analysis
    if social_media > 4:
        insights["critical"].append(f"CRITICAL: {social_media}h on social media - high addiction risk")
        insights["tips"].append("Delete social media apps, use browser version only")
    elif social_media > 2:
        insights["warnings"].append(f"WARNING: {social_media}h social media usage needs reduction")
        insights["tips"].append("Set specific times for social media (e.g., 6-7 PM only)")
    else:
        insights["positive"].append(f"GOOD: Healthy social media usage")
    
    # Gaming analysis
    if gaming_hours > 3:
        insights["warnings"].append(f"WARNING: {gaming_hours}h gaming is high")
        insights["tips"].append("Use gaming as reward after completing tasks")
    elif gaming_hours > 1:
        insights["positive"].append(f"OK: Moderate gaming is fine in balance")
    
    # Sleep analysis
    if sleep < 6:
        insights["critical"].append(f"CRITICAL: Only {sleep}h sleep - affects mental and physical health")
        insights["tips"].append("No phones 2 hours before bed, maintain consistent sleep schedule")
    elif sleep < 7:
        insights["warnings"].append(f"WARNING: {sleep}h sleep - aim for 7-8 hours")
        insights["tips"].append("Create bedtime routine: read, meditate, avoid screens")
    else:
        insights["positive"].append(f"GOOD: {sleep}h sleep supports brain function")
    
    # Study/Work analysis
    if study < 3:
        insights["critical"].append(f"CRITICAL: Only {study}h study time - productivity severely impacted")
        insights["tips"].append("Use Pomodoro technique: 25 min focus, 5 min break")
    elif study < 5:
        insights["warnings"].append(f"WARNING: {study}h study time could be increased")
        insights["tips"].append("Start with 2 hours of deep work daily")
    else:
        insights["positive"].append(f"GOOD: {study}h productive time is commendable")
    
    # Physical activity analysis
    if physical_activity < 0.5:
        insights["critical"].append(f"CRITICAL: Very low physical activity - health risk")
        insights["tips"].append("Start with 10-minute walks daily, gradually increase")
    elif physical_activity < 1:
        insights["warnings"].append(f"WARNING: Low physical activity")
        insights["tips"].append("Take stairs, walk during phone calls")
    else:
        insights["positive"].append(f"GOOD: Regular physical activity")
    
    # Family/Social time analysis
    if family_time < 1:
        insights["warnings"].append(f"WARNING: Low family or social interaction")
        insights["tips"].append("Schedule phone-free meals with family")
    elif family_time > 2:
        insights["positive"].append(f"GOOD: Quality time with loved ones")
    
    # Balance analysis
    total_screen = screen_time + gaming_hours
    productive_time = study + physical_activity + family_time
    
    if total_screen > productive_time * 2:
        insights["critical"].append(f"IMBALANCE: Screen time ({total_screen}h) dominates productive time ({productive_time}h)")
    elif total_screen > productive_time:
        insights["warnings"].append(f"IMBALANCE: Screen time slightly higher than productive activities")
    else:
        insights["positive"].append(f"BALANCE: Good balance between screen and productive time")
    
    return insights

def get_comprehensive_suggestions(score, screen_time, social_media, sleep, study, gaming_hours, physical_activity, family_time):
    suggestions = []
    
    # Score-based tiered suggestions
    if score >= 65:
        suggestions.append("URGENT INTERVENTION NEEDED")
        suggestions.append("-" * 30)
        suggestions.append("Reduce screen time by 3-4 hours immediately")
        suggestions.append("Install digital wellbeing apps to block apps after limit")
        suggestions.append("Keep phone in another room while sleeping")
        suggestions.append("Mandatory 4 hours of focused study or work daily")
        suggestions.append("Replace 1 hour of screen time with exercise")
        suggestions.append("Have all meals without phones or devices")
    elif score >= 35:
        suggestions.append("MODERATE RISK - ACTION RECOMMENDED")
        suggestions.append("-" * 30)
        suggestions.append("Reduce screen time by 1-2 hours gradually")
        suggestions.append("Use 45-15 rule: 45 min work, 15 min break")
        suggestions.append("No phones 1 hour before bed")
        suggestions.append("Increase study time by 1 hour daily")
        suggestions.append("30 minutes of physical activity daily")
    else:
        suggestions.append("HEALTHY ZONE - MAINTAIN AND IMPROVE")
        suggestions.append("-" * 30)
        suggestions.append("Continue your excellent digital habits")
        suggestions.append("Challenge yourself to increase productive time")
        suggestions.append("Share your routine with others struggling")
        suggestions.append("Set new personal growth goals")
    
    # Specific actionable tips
    suggestions.append("")
    suggestions.append("ACTIONABLE TIPS:")
    suggestions.append("-" * 30)
    
    if screen_time > 5:
        suggestions.append("Install 'Digital Wellbeing' or 'Screen Time' app")
        suggestions.append("Keep phone on grayscale mode (reduces appeal)")
        suggestions.append("Use website blockers during study hours")
    
    if social_media > 2:
        suggestions.append("Uninstall social media apps - use browser only")
        suggestions.append("Set 30-minute daily timer for social media")
        suggestions.append("Follow accounts that add value, unfollow distractions")
    
    if sleep < 7:
        suggestions.append("Create sleep sanctuary: dark, cool, quiet room")
        suggestions.append("Read physical books instead of scrolling before bed")
        suggestions.append("No caffeine after 4 PM")
    
    if study < 5:
        suggestions.append("Start with most important task (Eat That Frog technique)")
        suggestions.append("Use focus music or white noise")
        suggestions.append("Study in 25-min chunks with 5-min breaks")
    
    if physical_activity < 1:
        suggestions.append("Take 10-min walk after every meal")
        suggestions.append("Use standing desk or active workstation")
        suggestions.append("Join a group fitness class for accountability")
    
    if gaming_hours > 2:
        suggestions.append("Set gaming as reward after completing tasks")
        suggestions.append("Use timer before starting gaming session")
    
    suggestions.append("")
    suggestions.append("7-DAY CHALLENGE:")
    suggestions.append("-" * 30)
    suggestions.append("Day 1: Track all screen time")
    suggestions.append("Day 2: Reduce by 30 minutes")
    suggestions.append("Day 3: No phones during meals")
    suggestions.append("Day 4: 30 minutes exercise")
    suggestions.append("Day 5: Study in focused blocks")
    suggestions.append("Day 6: Screen-free 2 hours before bed")
    suggestions.append("Day 7: Reflect and plan next week")
    
    return suggestions

# Analyze button
if st.button("Analyze My Digital Health", type="primary"):
    
    score = calculate_score(screen_time, social_media, sleep, study, gaming_hours, physical_activity, family_time)
    risk_level, risk_color, risk_message = get_risk_level(score)
    insights = get_detailed_insights(screen_time, social_media, sleep, study, gaming_hours, physical_activity, family_time, score)
    
    # Display results
    st.markdown("---")
    st.subheader("Your Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Addiction Score", f"{score:.0f}/100")
        st.progress(score/100)
    
    with col2:
        st.markdown(f"<h3 style='color: {risk_color}'>Risk Level: {risk_level}</h3>", unsafe_allow_html=True)
        st.caption(risk_message)
    
    with col3:
        rating = 10 - (score / 10)
        st.metric("Lifestyle Rating", f"{round(rating,1)}/10")
    
    with col4:
        total_screen = screen_time + gaming_hours
        st.metric("Total Screen Time", f"{total_screen:.1f}h/day")
    
    # Critical Issues Section
    if insights["critical"]:
        st.markdown("---")
        st.subheader("Critical Issues - Immediate Attention Needed")
        for issue in insights["critical"]:
            st.error(issue)
    
    # Warnings Section
    if insights["warnings"]:
        st.markdown("---")
        st.subheader("Warning Signs")
        for warning in insights["warnings"]:
            st.warning(warning)
    
    # Positive Section
    if insights["positive"]:
        st.markdown("---")
        st.subheader("What You're Doing Well")
        for positive in insights["positive"]:
            st.success(positive)
    
    # Quick Tips
    if insights["tips"]:
        st.markdown("---")
        st.subheader("Quick Tips")
        for tip in insights["tips"]:
            st.info(tip)
    
    # Comprehensive Suggestions
    st.markdown("---")
    st.subheader("Personalized Recommendations")
    suggestions = get_comprehensive_suggestions(score, screen_time, social_media, sleep, study, gaming_hours, physical_activity, family_time)
    for suggestion in suggestions:
        if suggestion.startswith("-"):
            st.write(suggestion)
        elif suggestion == "":
            st.write("")
        else:
            st.markdown(f"**{suggestion}**" if suggestion in ["URGENT INTERVENTION NEEDED", "MODERATE RISK - ACTION RECOMMENDED", "HEALTHY ZONE - MAINTAIN AND IMPROVE", "ACTIONABLE TIPS:", "7-DAY CHALLENGE:"] else suggestion)
    
    # Graph - REDUCED SIZE
    st.markdown("---")
    st.subheader("Daily Habit Analysis")
    
    # Create smaller graph
    fig, ax = plt.subplots(figsize=(8, 4))  # Reduced from (10,6) to (8,4)
    labels = ['Screen', 'Social', 'Gaming', 'Sleep', 'Study', 'Exercise', 'Family']
    values = [screen_time, social_media, gaming_hours, sleep, study, physical_activity, family_time]
    colors = ['#ff6b6b', '#ff8c42', '#f9c74f', '#90be6d', '#577590', '#4c9f70', '#9c89b8']
    
    bars = ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_ylabel("Hours", fontsize=11)
    ax.set_title("Your Daily Habit Distribution", fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(max(values) + 2, 12))
    
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.1f}h', ha='center', va='bottom', fontsize=9)
    
    plt.xticks(rotation=45, fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    
    # AI Prediction
    try:
        prediction = predict_addiction([screen_time, social_media, sleep, study])
        st.markdown("---")
        st.subheader("AI Model Prediction")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Decision Tree Analysis:** {prediction} Risk")
        with col2:
            st.caption("Based on patterns from training data")
    except Exception as e:
        pass
    
    # Improvement Tracker
    st.markdown("---")
    st.subheader("30-Day Improvement Tracker")
    
    if score > 65:
        target = "Reduce score below 65"
        target_score = 65
    elif score > 35:
        target = "Reduce score below 35"
        target_score = 35
    else:
        target = "Maintain below 35"
        target_score = 35
    
    improvement_needed = max(0, score - target_score)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Score", f"{score:.0f}")
        st.metric("Target Score", f"{target_score:.0f}")
        st.metric("Improvement Needed", f"{improvement_needed:.0f} points")
    with col2:
        if improvement_needed > 0:
            st.write("**To reach your target:**")
            st.write(f"- Reduce screen time by {improvement_needed/8:.1f} hours")
            st.write(f"- Increase study by {improvement_needed/9:.1f} hours")
            st.write(f"- Improve sleep by {improvement_needed/6:.1f} hours")
    
    st.markdown("---")
    st.caption("Note: Consistency beats intensity. Small daily improvements lead to lasting change.")

else:
    st.info("Adjust the sliders above with your daily habits, then click 'Analyze My Digital Health' to get your comprehensive report.")
    
    st.subheader("What This Analyzer Does:")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Analysis Includes:**")
        st.write("- Addiction Score (0-100)")
        st.write("- Risk Level (Low/Medium/High)")
        st.write("- Lifestyle Rating (0-10)")
        st.write("- Critical Issues Detection")
        st.write("- Warning Signs")
        st.write("- Positive Habits")
    with col2:
        st.write("**You'll Receive:**")
        st.write("- Personalized Insights")
        st.write("- Actionable Suggestions")
        st.write("- 7-Day Challenge")
        st.write("- AI Model Prediction")
        st.write("- Improvement Tracker")
        st.write("- Habit Visualization")
    
    st.subheader("Sample Preview")
    sample_fig, sample_ax = plt.subplots(figsize=(8, 4))  # Reduced size for preview
    sample_labels = ['Screen', 'Social', 'Sleep', 'Study']
    sample_values = [6, 3, 6, 4]
    sample_ax.bar(sample_labels, sample_values, color=['#ff6b6b', '#ff8c42', '#90be6d', '#577590'])
    sample_ax.set_ylabel("Hours")
    sample_ax.set_title("Example: Moderate Digital Usage")
    plt.tight_layout()
    st.pyplot(sample_fig)