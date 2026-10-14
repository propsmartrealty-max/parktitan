#!/usr/bin/env python3
"""
scripts/upgrade_email_lead_dossier.py
Upgrades lead notification payloads across all enquiry forms to rich HTML format
with complete detailing for propsmartrealty@gmail.com.
1. index.html (handleEnq - modal & in-page contact forms)
2. functions/api/submit-lead.js (Cloudflare Pages edge function)
3. api/submit-lead.js (root serverless function)
4. functions/explore/[[slug]].js (programmatic SEO edge form)
"""

import re

def upgrade_index_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_payload_block = '''  const leadPayload = {
    _subject: `New Lead: ${rawName} (${cleanMobile}) - Park Titan Hinjewadi`,
    _replyto: rawEmail || "propsmartrealty@gmail.com",
    _captcha: "false",
    _template: "table",
    project: "Pride Purple Park Titan Hinjewadi",
    lead_name: rawName,
    contact_number: cleanMobile,
    email_address: rawEmail,
    configuration: rawConfig,
    budget_range: rawBudget,
    message: rawMsg,
    source_url: window.location.href,
    source_title: document.title,
    submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
  };'''

    new_payload_block = '''  const formattedTimestamp = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST';
  const whatsappUrl = 'https://wa.me/91' + cleanMobile + '?text=' + encodeURIComponent('Hi ' + rawName + ', thank you for your interest in Pride Purple Park Titan Hinjewadi. Sharing official brochure, floor plans & all-inclusive cost sheet.');
  const callUrl = 'tel:' + cleanMobile;

  const htmlDossier = '<div style="font-family:Arial,Helvetica,sans-serif;max-width:680px;background:#ffffff;border:1px solid #e0e0e0;border-radius:8px;padding:24px;margin:0 auto;color:#222222;box-shadow:0 4px 12px rgba(0,0,0,0.06);">' +
    '<div style="border-bottom:3px solid #C8963C;padding-bottom:14px;margin-bottom:18px;">' +
      '<span style="background:#3B1540;color:#E6BE6E;font-size:11px;font-weight:bold;padding:4px 10px;border-radius:4px;letter-spacing:1px;text-transform:uppercase;">OFFICIAL VERIFIED LEAD</span>' +
      '<h2 style="margin:10px 0 4px;color:#1a1a1a;font-size:22px;font-weight:700;">Pride Purple Park Titan Hinjewadi</h2>' +
      '<p style="margin:0;font-size:13px;color:#666;">New Buyer Enquiry Dispatched to Sales Desk (propsmartrealty@gmail.com)</p>' +
    '</div>' +
    '<h3 style="font-size:15px;color:#3B1540;margin:18px 0 8px;text-transform:uppercase;letter-spacing:0.5px;">1. Prospective Buyer Profile</h3>' +
    '<table style="width:100%;border-collapse:collapse;margin-bottom:18px;font-size:13px;">' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;width:38%;">Full Name</td><td style="padding:10px;border:1px solid #eee;font-size:14px;font-weight:bold;color:#111;">' + rawName + '</td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Contact Phone</td><td style="padding:10px;border:1px solid #eee;"><a href="' + callUrl + '" style="color:#C8963C;font-weight:bold;text-decoration:none;font-size:14px;">📞 +91 ' + cleanMobile + '</a></td></tr>' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">WhatsApp Click-to-Chat</td><td style="padding:10px;border:1px solid #eee;"><a href="' + whatsappUrl + '" style="display:inline-block;background:#25D366;color:#ffffff;font-weight:bold;padding:6px 14px;border-radius:4px;text-decoration:none;font-size:12px;">💬 Chat with ' + rawName + ' on WhatsApp</a></td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Email Address</td><td style="padding:10px;border:1px solid #eee;">' + (rawEmail ? '<a href="mailto:' + rawEmail + '" style="color:#2980b9;">' + rawEmail + '</a>' : '<span style="color:#888;">Not Provided</span>') + '</td></tr>' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Interested Configuration</td><td style="padding:10px;border:1px solid #eee;font-weight:bold;color:#2c3e50;">' + rawConfig + '</td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Budget Range (Final Price)</td><td style="padding:10px;border:1px solid #eee;font-weight:bold;color:#27ae60;">' + rawBudget + '</td></tr>' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Customer Message / Visit Notes</td><td style="padding:10px;border:1px solid #eee;color:#333;">' + (rawMsg ? rawMsg : '<em>Immediate Site Visit &amp; Sanctioned Cost Sheet Requested</em>') + '</td></tr>' +
    '</table>' +
    '<h3 style="font-size:15px;color:#3B1540;margin:18px 0 8px;text-transform:uppercase;letter-spacing:0.5px;">2. Project &amp; Regulatory Specifications</h3>' +
    '<table style="width:100%;border-collapse:collapse;margin-bottom:18px;font-size:13px;">' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;width:38%;">Township Project</td><td style="padding:10px;border:1px solid #eee;">Pride Purple Park Titan (18 Towers across 17+ Acres)</td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Project Address</td><td style="padding:10px;border:1px solid #eee;">Hinjewadi-Marunji Link Road, Phase 1, Hinjewadi, Pune 411057</td></tr>' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">MahaRERA Registration</td><td style="padding:10px;border:1px solid #eee;">Phase 1 (P52100028049) · Phase 2 (P52100030567) · Phase 5 (P52100047702)</td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Sanctioned Carpet Sizes</td><td style="padding:10px;border:1px solid #eee;">2 BHK: 726.44 &amp; 789.54 sq.ft. | 3 BHK: 988.25, 1,059.87 &amp; 1,212.22 sq.ft.</td></tr>' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Final All-Inclusive Price</td><td style="padding:10px;border:1px solid #eee;color:#27ae60;font-weight:bold;">₹93.57 Lakhs* to ₹1.65 Crore* (Zero Agreement Value Mention)</td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Key Infrastructure</td><td style="padding:10px;border:1px solid #eee;">7-Acre Raised Vehicle-Free Podium, 5 On-Site Academies (Badminton, Swim, Dance, Sports, Music)</td></tr>' +
    '</table>' +
    '<h3 style="font-size:15px;color:#3B1540;margin:18px 0 8px;text-transform:uppercase;letter-spacing:0.5px;">3. Source &amp; Digital Tracking Metadata</h3>' +
    '<table style="width:100%;border-collapse:collapse;margin-bottom:18px;font-size:13px;">' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;width:38%;">Lead Captured At</td><td style="padding:10px;border:1px solid #eee;">' + formattedTimestamp + '</td></tr>' +
      '<tr style="background:#ffffff;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Landing Page URL</td><td style="padding:10px;border:1px solid #eee;"><a href="' + window.location.href + '" style="color:#2980b9;">' + window.location.href + '</a></td></tr>' +
      '<tr style="background:#fcfcfc;"><td style="padding:10px;border:1px solid #eee;font-weight:600;">Page Title</td><td style="padding:10px;border:1px solid #eee;">' + document.title + '</td></tr>' +
    '</table>' +
    '<div style="background:#ebf5fb;border-left:4px solid #2980b9;padding:14px;border-radius:4px;font-size:13px;color:#1b4f72;">' +
      '<strong>⚡ IMMEDIATE ACTION REQUIRED:</strong> Call <strong>' + rawName + '</strong> at <a href="' + callUrl + '" style="color:#2980b9;font-weight:bold;">' + cleanMobile + '</a> within 15 minutes. Dispatch sanctioned brochure &amp; cost sheet on WhatsApp.' +
    '</div>' +
  '</div>';

  const leadPayload = {
    _subject: '🔥 HIGH-INTENT LEAD: ' + rawName + ' (' + cleanMobile + ') | ' + rawConfig + ' | Park Titan Hinjewadi',
    _replyto: rawEmail || 'propsmartrealty@gmail.com',
    _captcha: 'false',
    _template: 'table',
    '01_Lead_Full_Name': rawName,
    '02_Contact_Number': cleanMobile,
    '03_WhatsApp_Direct_Chat': whatsappUrl,
    '04_One_Click_Call': callUrl,
    '05_Email_Address': rawEmail || 'Not Provided',
    '06_Interested_Configuration': rawConfig,
    '07_All_Inclusive_Budget_Range': rawBudget,
    '08_Customer_Message_Notes': rawMsg || 'Immediate Site Visit & Official Cost Sheet Requested',
    '09_Target_Project': 'Pride Purple Park Titan (18 Towers on 17+ Acres)',
    '10_Project_Location': 'Hinjewadi-Marunji Link Road, Phase 1, Hinjewadi, Pune 411057',
    '11_MahaRERA_Numbers': 'Phase 1 (P52100028049) | Phase 2 (P52100030567) | Phase 5 (P52100047702)',
    '12_Sanctioned_Carpet_Sizes': '2 BHK (726.44 & 789.54 sq.ft.) | 3 BHK (988.25, 1,059.87 & 1,212.22 sq.ft.)',
    '13_Price_Spectrum_Final_Price': '₹93.57 Lakhs* to ₹1.65 Crore* (Final Price Only)',
    '14_Landing_Page_URL': window.location.href,
    '15_Page_Title': document.title,
    '16_Submission_Timestamp_IST': formattedTimestamp,
    '17_Recommended_Action': 'Call ' + cleanMobile + ' within 15 mins or chat on WhatsApp',
    '18_Complete_HTML_Lead_Dossier': htmlDossier
  };'''

    assert old_payload_block in content, "Could not match old_payload_block in index.html"
    content = content.replace(old_payload_block, new_payload_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html upgraded with rich HTML lead dossier!")

def upgrade_edge_function(path):
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    old_block = '''      const emailContent = {
        _subject: `New Lead: ${leadPayload.name} (${leadPayload.mobile}) - Park Titan Hinjewadi`,
        _replyto: leadPayload.email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        project: leadPayload.project,
        lead_name: leadPayload.name,
        contact_number: leadPayload.mobile,
        email_address: leadPayload.email,
        interested_configuration: leadPayload.configuration,
        budget_range: leadPayload.budget,
        visitor_message: leadPayload.message,
        source_url: leadPayload.source_url,
        source_title: leadPayload.source_title,
        timestamp: leadPayload.timestamp,
        client_country: leadPayload.country
      };'''

    if old_block in code:
        new_block = '''      const formattedTime = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST';
      const waUrl = 'https://wa.me/91' + cleanMobile + '?text=' + encodeURIComponent('Hi ' + leadPayload.name + ', thank you for your enquiry regarding Pride Purple Park Titan Hinjewadi. Sharing official cost sheet & floor plans.');
      const telUrl = 'tel:' + cleanMobile;

      const emailContent = {
        _subject: `🔥 HIGH-INTENT LEAD: ${leadPayload.name} (${cleanMobile}) | ${leadPayload.configuration} | Park Titan Hinjewadi`,
        _replyto: leadPayload.email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        "01_Lead_Full_Name": leadPayload.name,
        "02_Contact_Number": cleanMobile,
        "03_WhatsApp_Direct_Chat": waUrl,
        "04_One_Click_Call": telUrl,
        "05_Email_Address": leadPayload.email || "Not Provided",
        "06_Interested_Configuration": leadPayload.configuration,
        "07_All_Inclusive_Budget_Range": leadPayload.budget,
        "08_Customer_Message_Notes": leadPayload.message || "Immediate Site Visit & Official Cost Sheet Requested",
        "09_Target_Project": "Pride Purple Park Titan (18 Towers across 17+ Acres)",
        "10_Project_Location": "Hinjewadi-Marunji Link Road, Phase 1, Hinjewadi, Pune 411057",
        "11_MahaRERA_Numbers": "Phase 1: P52100028049 | Phase 2: P52100030567 | Phase 5: P52100047702",
        "12_Sanctioned_Carpet_Sizes": "2 BHK (726.44 & 789.54 sq.ft.) | 3 BHK (988.25, 1,059.87 & 1,212.22 sq.ft.)",
        "13_Price_Spectrum_Final_Price": "₹93.57 Lakhs* to ₹1.65 Crore* (Final Price Only)",
        "14_Landing_Page_URL": leadPayload.source_url,
        "15_Page_Title": leadPayload.source_title,
        "16_Submission_Timestamp_IST": formattedTime,
        "17_Client_IP": leadPayload.client_ip,
        "18_Client_Country": leadPayload.country,
        "19_Recommended_Action": `Call ${cleanMobile} within 15 minutes or message on WhatsApp`
      };'''
        code = code.replace(old_block, new_block)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"{path} upgraded successfully!")
    else:
        print(f"Warning: could not find old_block in {path}")

def upgrade_api_root():
    path = 'api/submit-lead.js'
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    old_block = '''      const emailContent = {
        _subject: `New Lead: ${leadPayload.name} (${leadPayload.configuration}) - Park Titan Hinjewadi`,
        _replyto: leadPayload.email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        project: leadPayload.project,
        lead_name: leadPayload.name,
        contact_number: leadPayload.mobile,
        email_address: leadPayload.email,
        interested_configuration: leadPayload.configuration,
        budget_range: leadPayload.budget,
        visitor_message: leadPayload.message,
        source_url: leadPayload.source,
        timestamp: leadPayload.timestamp,
        client_country: leadPayload.country
      };'''

    if old_block in code:
        new_block = '''      const formattedTime = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST';
      const waUrl = 'https://wa.me/91' + data.mobile + '?text=' + encodeURIComponent('Hi ' + leadPayload.name + ', thank you for your enquiry regarding Pride Purple Park Titan Hinjewadi. Sharing official cost sheet & floor plans.');
      const telUrl = 'tel:' + data.mobile;

      const emailContent = {
        _subject: `🔥 HIGH-INTENT LEAD: ${leadPayload.name} (${data.mobile}) | ${leadPayload.configuration} | Park Titan Hinjewadi`,
        _replyto: leadPayload.email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        "01_Lead_Full_Name": leadPayload.name,
        "02_Contact_Number": data.mobile,
        "03_WhatsApp_Direct_Chat": waUrl,
        "04_One_Click_Call": telUrl,
        "05_Email_Address": leadPayload.email || "Not Provided",
        "06_Interested_Configuration": leadPayload.configuration,
        "07_All_Inclusive_Budget_Range": leadPayload.budget,
        "08_Customer_Message_Notes": leadPayload.message || "Immediate Site Visit & Official Cost Sheet Requested",
        "09_Target_Project": "Pride Purple Park Titan (18 Towers across 17+ Acres)",
        "10_Project_Location": "Hinjewadi-Marunji Link Road, Phase 1, Hinjewadi, Pune 411057",
        "11_MahaRERA_Numbers": "Phase 1: P52100028049 | Phase 2: P52100030567 | Phase 5: P52100047702",
        "12_Sanctioned_Carpet_Sizes": "2 BHK (726.44 & 789.54 sq.ft.) | 3 BHK (988.25, 1,059.87 & 1,212.22 sq.ft.)",
        "13_Price_Spectrum_Final_Price": "₹93.57 Lakhs* to ₹1.65 Crore* (Final Price Only)",
        "14_Landing_Page_URL": leadPayload.source,
        "15_Submission_Timestamp_IST": formattedTime,
        "16_Client_IP": leadPayload.client_ip,
        "17_Client_Country": leadPayload.country,
        "18_Recommended_Action": `Call ${data.mobile} within 15 minutes or message on WhatsApp`
      };'''
        code = code.replace(old_block, new_block)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"{path} upgraded successfully!")

def upgrade_explore_slug():
    path = 'functions/explore/[[slug]].js'
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    old_block = '''      const payload = {
        _subject: 'New Lead: ' + name + ' (' + phone + ') - Park Titan Explore Page',
        _replyto: email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        project: "Pride Purple Park Titan Hinjewadi",
        lead_name: name,
        contact_number: phone,
        email_address: email,
        configuration: config,
        source_url: window.location.href,
        submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
      };'''

    if old_block in code:
        new_block = '''      const formattedTime = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST';
      const waUrl = 'https://wa.me/91' + phone + '?text=' + encodeURIComponent('Hi ' + name + ', thank you for your enquiry regarding Pride Purple Park Titan Hinjewadi. Sharing official cost sheet & floor plans.');
      const telUrl = 'tel:' + phone;

      const payload = {
        _subject: '🔥 HIGH-INTENT LEAD: ' + name + ' (' + phone + ') | ' + config + ' | Park Titan Programmatic Explore',
        _replyto: email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        "01_Lead_Full_Name": name,
        "02_Contact_Number": phone,
        "03_WhatsApp_Direct_Chat": waUrl,
        "04_One_Click_Call": telUrl,
        "05_Email_Address": email || "Not Provided",
        "06_Interested_Configuration": config,
        "07_Final_Price_Budget": "₹93.57L* - ₹1.65 Cr* (All-Inclusive Final Price)",
        "08_Target_Project": "Pride Purple Park Titan (18 Towers across 17+ Acres)",
        "09_Project_Location": "Hinjewadi-Marunji Link Road, Phase 1, Hinjewadi, Pune 411057",
        "10_MahaRERA_Numbers": "Phase 1: P52100028049 | Phase 2: P52100030567 | Phase 5: P52100047702",
        "11_Sanctioned_Carpet_Sizes": "2 BHK (726.44 & 789.54 sq.ft.) | 3 BHK (988.25, 1,059.87 & 1,212.22 sq.ft.)",
        "12_Landing_Page_URL": window.location.href,
        "13_Page_Title": document.title,
        "14_Submission_Timestamp_IST": formattedTime,
        "15_Recommended_Action": "Call " + phone + " within 15 minutes or message on WhatsApp"
      };'''
        code = code.replace(old_block, new_block)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"{path} upgraded successfully!")

if __name__ == '__main__':
    upgrade_index_html()
    upgrade_edge_function('functions/api/submit-lead.js')
    upgrade_api_root()
    upgrade_explore_slug()
