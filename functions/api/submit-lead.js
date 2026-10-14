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
      const emailContent = {
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
