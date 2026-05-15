---
layout: default
title: Connect
permalink: /connect/
description: "Scan to follow Moorabbin Kangaroos FC online — website and all social media in one place with QR codes. Print or save as PDF."
---

<style>
.connect-page {
  max-width: 960px;
  margin: 0 auto;
  padding-bottom: 2rem;
}

.connect-intro {
  text-align: center;
  margin-bottom: 1.5rem;
}

.connect-intro h1 {
  margin-bottom: 0.5rem;
}

.connect-intro p {
  color: #555;
  margin: 0 auto;
  max-width: 620px;
}

.connect-print-actions {
  text-align: center;
  margin: 1rem 0 2rem;
}

.connect-print-button {
  display: inline-block;
  background-color: #013087;
  color: #fff !important;
  padding: 0.6rem 1.4rem;
  border-radius: 4px;
  font-weight: 700;
  text-decoration: none !important;
  font-size: 0.95rem;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.connect-print-button:hover {
  background-color: #001a5e;
}

.connect-website {
  background: linear-gradient(135deg, #013087 0%, #1F4DA8 100%);
  color: #fff;
  border-radius: 8px;
  padding: 2rem;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.connect-website-info {
  flex: 1 1 280px;
  text-align: center;
}

.connect-website-info h2 {
  color: #fff;
  margin: 0 0 0.5rem;
  font-size: 1.9rem;
}

.connect-website-info .connect-website-url {
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0 0 0.75rem;
  letter-spacing: 0.02em;
}

.connect-website-info .connect-website-blurb {
  color: #C8D6F0;
  margin: 0;
  font-size: 0.95rem;
}

.connect-website-qr {
  background: #fff;
  padding: 14px;
  border-radius: 6px;
  width: 220px;
  height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
}

.connect-website-qr svg {
  width: 100%;
  height: 100%;
  display: block;
}

.connect-section-heading {
  text-align: center;
  margin: 0 0 1.25rem;
  color: #013087;
  border-bottom: 2px solid #C8D6F0;
  padding-bottom: 0.5rem;
}

.connect-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1.25rem;
}

.connect-card {
  border: 1px solid #C8D6F0;
  border-radius: 8px;
  padding: 1rem 0.75rem;
  text-align: center;
  background: #fff;
  break-inside: avoid;
  page-break-inside: avoid;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.connect-card-platform {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  justify-content: center;
  margin-bottom: 0.5rem;
}

.connect-card-platform img {
  width: 22px;
  height: 22px;
  display: block;
}

.connect-card-platform h3 {
  margin: 0;
  font-size: 1.05rem;
  color: #013087;
}

.connect-card-qr {
  width: 150px;
  height: 150px;
  margin: 0.25rem auto 0.5rem;
  background: #fff;
  padding: 6px;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.connect-card-qr svg {
  width: 100%;
  height: 100%;
  display: block;
}

.connect-card-handle {
  font-weight: 700;
  color: #013087;
  font-size: 0.9rem;
  word-break: break-word;
}

.connect-card-url {
  font-size: 0.72rem;
  color: #666;
  margin-top: 0.2rem;
  word-break: break-all;
  line-height: 1.3;
}

.connect-footer-note {
  text-align: center;
  color: #777;
  font-size: 0.85rem;
  margin-top: 2rem;
}

/* Print styles — clean output for PDF export */
@media print {
  .site-header,
  .site-footer,
  .site-nav,
  .connect-print-actions {
    display: none !important;
  }

  body {
    background: #fff !important;
    color: #000;
    font-size: 9pt;
  }

  .page-content {
    padding: 0 !important;
  }

  .wrapper {
    max-width: none !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  .connect-page {
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .connect-intro {
    margin-bottom: 0.5rem;
  }

  .connect-intro h1 {
    font-size: 18pt;
    margin: 0 0 0.2rem;
  }

  .connect-intro p,
  .connect-card-url {
    color: #333 !important;
  }

  .connect-intro p {
    font-size: 9pt;
    margin: 0 auto;
  }

  .connect-website {
    background: #013087 !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    page-break-inside: avoid;
    break-inside: avoid;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.9rem;
    gap: 1.2rem;
  }

  .connect-website-info h2 {
    font-size: 15pt;
    margin: 0 0 0.2rem;
  }

  .connect-website-info .connect-website-url {
    font-size: 12pt;
    margin: 0 0 0.3rem;
  }

  .connect-website-info .connect-website-blurb {
    color: #fff !important;
    font-size: 9pt;
  }

  .connect-website-qr {
    width: 110px;
    height: 110px;
    padding: 6px;
  }

  .connect-section-heading {
    font-size: 12pt;
    margin: 0 0 0.6rem;
    padding-bottom: 0.25rem;
  }

  .connect-card {
    page-break-inside: avoid;
    break-inside: avoid;
    border: 1px solid #888;
    padding: 0.4rem 0.3rem;
  }

  .connect-card-platform {
    margin-bottom: 0.25rem;
    gap: 0.3rem;
  }

  .connect-card-platform h3 {
    font-size: 9pt;
  }

  .connect-card-platform img,
  .connect-card-platform svg {
    width: 14px !important;
    height: 14px !important;
  }

  .connect-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 0.4rem;
  }

  .connect-card-qr {
    width: 95px;
    height: 95px;
    margin: 0.15rem auto 0.3rem;
    padding: 3px;
  }

  .connect-card-handle {
    font-size: 8pt;
  }

  .connect-card-url {
    font-size: 6.5pt;
    margin-top: 0.1rem;
  }

  .connect-footer-note {
    font-size: 7.5pt;
    margin-top: 0.8rem;
  }

  @page {
    margin: 10mm;
    size: A4;
  }

  h1, h2, h3 {
    page-break-after: avoid;
  }
}
</style>

<div class="connect-page">

<div class="connect-intro">
<h1>Connect with Moorabbin Kangaroos FC</h1>
<p>Scan a code with your phone camera to visit our website or follow us on social media. Print this page or save it as a PDF to share around the club.</p>
</div>

<div class="connect-print-actions">
  <button type="button" class="connect-print-button" onclick="window.print()">Print or Save as PDF</button>
</div>

<div class="connect-website">
  <div class="connect-website-info">
    <h2>Visit our Website</h2>
    <p class="connect-website-url">www.mkfc.org.au</p>
    <p class="connect-website-blurb">Fixtures, news, players, history, sponsors — everything Moorabbin Kangaroos.</p>
  </div>
  <div class="connect-website-qr" data-qr="https://www.mkfc.org.au"></div>
</div>

<h2 class="connect-section-heading">Follow us on Social Media</h2>

<div class="connect-grid">

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/facebook/013087" alt="" loading="lazy">
      <h3>Facebook</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://www.facebook.com/MoorabbinKangas"></div>
    <div class="connect-card-handle">MoorabbinKangas</div>
    <div class="connect-card-url">facebook.com/MoorabbinKangas</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/instagram/013087" alt="" loading="lazy">
      <h3>Instagram</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://www.instagram.com/moorabbinkangas"></div>
    <div class="connect-card-handle">@moorabbinkangas</div>
    <div class="connect-card-url">instagram.com/moorabbinkangas</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/x/013087" alt="" loading="lazy">
      <h3>X (Twitter)</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://x.com/moorabbinkangas"></div>
    <div class="connect-card-handle">@moorabbinkangas</div>
    <div class="connect-card-url">x.com/moorabbinkangas</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/youtube/013087" alt="" loading="lazy">
      <h3>YouTube</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://www.youtube.com/@MoorabbinKangas"></div>
    <div class="connect-card-handle">@MoorabbinKangas</div>
    <div class="connect-card-url">youtube.com/@MoorabbinKangas</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/tiktok/013087" alt="" loading="lazy">
      <h3>TikTok</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://www.tiktok.com/@moorabbinkangas"></div>
    <div class="connect-card-handle">@moorabbinkangas</div>
    <div class="connect-card-url">tiktok.com/@moorabbinkangas</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/threads/013087" alt="" loading="lazy">
      <h3>Threads</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://www.threads.com/@moorabbinkangas"></div>
    <div class="connect-card-handle">@moorabbinkangas</div>
    <div class="connect-card-url">threads.com/@moorabbinkangas</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <img src="https://cdn.simpleicons.org/bluesky/013087" alt="" loading="lazy">
      <h3>Bluesky</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://bsky.app/profile/moorabbinkangas.bsky.social"></div>
    <div class="connect-card-handle">@moorabbinkangas.bsky.social</div>
    <div class="connect-card-url">bsky.app/profile/moorabbinkangas.bsky.social</div>
  </div>

  <div class="connect-card">
    <div class="connect-card-platform">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#013087" aria-hidden="true" style="width:22px;height:22px;display:block;"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.852 3.37-1.852 3.601 0 4.267 2.37 4.267 5.455v6.288zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.063 2.063 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      <h3>LinkedIn</h3>
    </div>
    <div class="connect-card-qr" data-qr="https://www.linkedin.com/company/moorabbinkangas"></div>
    <div class="connect-card-handle">moorabbinkangas</div>
    <div class="connect-card-url">linkedin.com/company/moorabbinkangas</div>
  </div>

</div>

<p class="connect-footer-note">Moorabbin Kangaroos Football Club &middot; Widdop Crescent Oval, Hampton East VIC 3188 &middot; info@mkfc.org.au</p>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
<script>
(function() {
  function renderQRs() {
    if (typeof qrcode !== 'function') return;
    document.querySelectorAll('[data-qr]').forEach(function(el) {
      if (el.dataset.qrRendered === '1') return;
      var url = el.getAttribute('data-qr');
      if (!url) return;
      var qr = qrcode(0, 'M');
      qr.addData(url);
      qr.make();
      el.innerHTML = qr.createSvgTag({ cellSize: 4, margin: 0, scalable: true });
      var svg = el.querySelector('svg');
      if (svg) {
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        svg.style.width = '100%';
        svg.style.height = '100%';
      }
      el.dataset.qrRendered = '1';
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderQRs);
  } else {
    renderQRs();
  }
})();
</script>
