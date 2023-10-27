from swarms.models.bing_chat import BingChat
# Initialize the EdgeGPTModel
bing = BingChat(cookies_path="./cookies.json")
task = "generate topics for PositiveMed.com,:  1. Monitor Health Trends: Scan Google Alerts, authoritative health websites, and social media for emerging health, wellness, and medical discussions. 2. Keyword Research: Utilize tools like SEMrush to identify keywords with moderate to high search volume and low competition. Focus on long-tail, conversational keywords. 3. Analyze Site Data: Review PositiveMed's analytics to pinpoint popular articles and areas lacking recent content. 4. Crowdsourcing: Gather topic suggestions from the brand's audience and internal team, ensuring alignment with PositiveMed's mission. 5. Topic Evaluation: Assess topics for audience relevance, uniqueness, brand fit, current relevance, and SEO potential. 6. Tone and Style: Ensure topics can be approached with an educational, empowering, and ethical tone, in line with the brand's voice.  Use this framework to generate a list of potential topics that cater to PositiveMed's audience while staying true to its brand ethos.  Find trending topics for slowing and reversing aging think step by step and o into as much detail as possible"
response = bing(task)

print(response)
