## Inspiration
Have either of the following happened to you?
* Ever since elementary school you've been fascinated by 17th century Turkish ethnography. Luckily, you just discovered a preeminent historian's blog about the collapse of the Ottoman Empire. Overjoyed, you start to text your friends, but soon remember that they're into 19th century Victorian poetry. If only you could share your love of historical discourse with another intellectual.
* Because you're someone with good taste, you're browsing Buzzfeed. Somehow "27 Extremely Disturbing Wikipedia Pages That Will Haunt Your Dreams" is not cutting it for you. Dang. If only you could see what your best friend Alicia was browsing. She would definitely know how to help you procrastinate on your TreeHacks project. 

Great! Because we built Pagechat for you. We all have unique interests, many of which are expressed through our internet browsing. We believe that building simple connections through those interests is a powerful way to improve well-being. We built an _convenient_ and _efficient_ tool to connect people through their internet browsing.
## What it does
Pagechat is a Google Chrome extension designed to promote serendipituous connections by offering one-on-one text chats centered on internet browsing. When active, Pagechat
* displays what you are your friends are currently reading, allowing you to discover and share interesting articles
* centers the conversation around webpages by giving friends the opportunity to chat each other directly through Chrome
* intelligently connects users with similar interests by creating one-on-one chats for users visiting the same webpage

## How we built it
### Chatting
### User Recommendations
If several people are browsing the same website and want to chat with each other, how do we pair them up? Intuitively, people who have similar browsing histories will have more in common to talk about, so we should group them together. We maintain a dynamic **feature vector** for each user In order to intelligently match users who are on the same webpage, we store a dynamic feature vector for each user logged in to Pagechat.
## What's next for Pagechat
Yee