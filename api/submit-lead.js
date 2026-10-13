/**
 * Cloudflare Pages Serverless Function: /api/submit-lead
 * Handles lead submissions, validates payload, dispatches email to propsmartrealty@gmail.com,
 * and returns instant direct desk response (+91 7744009295).
 */
export async function onRequestPost(context) {
  try {
    const data = await context.request.json();
    
    // Validation
    if (!data.mobile || data.mobile.length !== 10) {
      return new Response(JSON.stringify({ success: false, message: "Valid 10-digit mobile number required" }), {
        status: 400,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }

    const leadPayload = {
      project: "Pride Purple Park Titan Hinjewadi",
      name: data.name || "Website Visitor",
      mobile: data.mobile,
      email: data.email || "",
      configuration: data.config || "2/3 BHK",
      budget: data.budget || "₹90L - ₹1.50Cr",
      message: data.msg || "",
      recipient_email: "propsmartrealty@gmail.com",
      source: "https://purpleparktitan.com",
      timestamp: new Date().toISOString(),
      client_ip: context.request.headers.get("CF-Connecting-IP") || "",
      country: context.request.headers.get("CF-IPCountry") || "IN"
    };

    // Forward lead notification email to propsmartrealty@gmail.com via reliable email dispatcher
    try {
      const emailContent = {
        _subject: `New Lead: ${leadPayload.name} (${leadPayload.configuration}) - Park Titan Hinjewadi`,
        _replyto: leadPayload.email || "propsmartrealty@gmail.com",
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
      };

      // Dispatch async lead alert to propsmartrealty@gmail.com
      await fetch("https://formsubmit.co/ajax/propsmartrealty@gmail.com", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(emailContent)
      });
    } catch (emailErr) {
      // Non-blocking fallback
      console.error("Lead email dispatch error:", emailErr);
    }

    // Return success response with updated phone and WhatsApp (7744009295)
    return new Response(JSON.stringify({
      success: true,
      message: "Enquiry submitted successfully. Your request has been forwarded to propsmartrealty@gmail.com. Our specialist will call you shortly.",
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
      headers: { "Content-Type": "application/json" }
    });
  }
}
