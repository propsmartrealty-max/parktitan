/**
 * Cloudflare Pages Serverless Function: /api/submit-lead
 * Handles lead submissions, validates payload, dispatches email to propsmartrealty@gmail.com,
 * and returns instant direct desk response (+91 7744009295).
 */

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400"
    }
  });
}

export async function onRequestPost(context) {
  try {
    const data = await context.request.json();
    
    // Normalize mobile / phone input
    const rawMobile = data.mobile || data.phone || "";
    const cleanMobile = rawMobile.replace(/[^0-9]/g, "").slice(-10);

    // Validation
    if (!cleanMobile || cleanMobile.length !== 10) {
      return new Response(JSON.stringify({
        success: false,
        message: "Valid 10-digit mobile number required"
      }), {
        status: 400,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }

    const leadPayload = {
      project: "Pride Purple Park Titan Hinjewadi",
      name: data.name || "Website Visitor",
      mobile: cleanMobile,
      email: data.email || "",
      configuration: data.config || data.configuration || "2/3 BHK",
      budget: data.budget || "₹93.57L - ₹1.64Cr (All-Inclusive)",
      message: data.msg || data.message || "",
      recipient_email: "propsmartrealty@gmail.com",
      source_url: data.url || "https://purpleparktitan.com",
      source_title: data.title || "Pride Purple Park Titan Official Portal",
      timestamp: new Date().toISOString(),
      client_ip: context.request.headers.get("CF-Connecting-IP") || "",
      country: context.request.headers.get("CF-IPCountry") || "IN"
    };

    // Forward lead notification email to propsmartrealty@gmail.com
    try {
      const formattedTime = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST';
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
      };

      await fetch("https://formsubmit.co/ajax/propsmartrealty@gmail.com", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(emailContent)
      });
    } catch (emailErr) {
      console.error("Lead email dispatch error:", emailErr);
    }

    // Return success response with direct sales desk info
    return new Response(JSON.stringify({
      success: true,
      message: "Enquiry submitted successfully. Your request has been forwarded to our Park Titan sales desk. A specialist will call you shortly.",
      lead_id: "PT-" + Math.floor(100000 + Math.random() * 900000),
      direct_sales_phone: "+91-7744009295",
      whatsapp: "https://wa.me/917744009295"
    }), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Cache-Control": "no-store"
      }
    });

  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), {
      status: 500,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      }
    });
  }
}
