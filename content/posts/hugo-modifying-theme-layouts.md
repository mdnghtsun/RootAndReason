---
title: "Overriding Hugo Theme Layouts"
date: '2025-06-22T20:55:00-07:00'
draft: false
tags: ["hugo", "coding", "webdev"]
---

If you're using a Hugo theme like [PaperMod](https://github.com/adityatelange/hugo-PaperMod) and want to customize part of its layout, the correct way to do this is by overriding the theme’s templates locally — without modifying the theme directly.

This approach lets you:

- Add custom content (e.g., footers, notices) to specific post types
- Preserve your changes even if the theme updates
- Keep the theme code clean and version-controlled

For my purposes, I wanted to extended the behavior of the PaperMod theme I'm using to include a mention about amazon afiliate links in the page footers -- without overriding the default footer containing information on how the site was built (hugo + paper mod, etc). 

So there was a bit of work to do and a learning curve that ChatGPT defintely helped me understand (though it could have been more verbose in its explanations). I am writing this post here as my own set of personal note and to help explain how all this works other others.

Goal: Show an Amazon affiliate disclaimer only for posts that need it — while preserving the regular site-wide footer.

---

## 0. Understand Hugo’s Lookup Order

Hugo looks for templates in your root `layouts/` directory **before** checking the theme. So you can override any theme partial or template by recreating its file path in your own project:

```bash
layouts/_default/single.html           # Overrides the default layout for single content pages
layouts/partials/footer.html           # Overrides the global footer
layouts/partials/content-footer.html   # Custom footer we’ll inject in posts when amazon affiliate links are present
```

## 1. Create layouts/_default/single.html

single.html controls what renders under each post. I overrode the theme default by creating the follwing file under layouts/_default/single.html:

```
{{ define "main" }}
  {{- partial "content.html" . }}
  {{- partial "content-footer.html" . }}
{{ end }}
```

This reuses the theme’s default content.html, then calls our custom content-footer.html for affiliate disclaimers, effectively overriding the default behavior of the theme. 

## 2. Create layouts/partials/content-footer.html

Here we conditionally render a disclaimer based on a frontmatter flag.
```
{{ if and (.IsPage) (eq .Type "posts") (.Params.affiliate) }}
<footer class="footer">
  <div class="container">
    <p style="font-size: 0.8em; color: #888; text-align: center;">
      Disclosure: As an Amazon Associate, I earn from qualifying purchases.
    </p>
  </div>
</footer>
{{ end }}
```
What's happening here is we're defining the content-footer noted above in Step 2. 

Since I wanted this footer to only show up on posts where I had an amazon affiliate link, I included a conditional before the HTML that checks the posts frontmatter for a parameter 'affilate' before rendering. 

## 3. Reference/Toggle the Custom Header
Finally, in the post md file itself, ensure that the frontmatter sets `affiliate: true`. This ensures that Hugo correctly notes the post as requiring the content footer we've previusly defined. 

As an example:
```
---
title: "This is a Post"
date: 2025-07-09
tags: ["blah", "blob", "blur"]
affiliate: true
---
```

An example of the change made here (i.e. custom amazon affiliate footer) can be viewed in my previous post [Ali: The Elixir of Love](https://mdnghtsun.github.io/RootAndReason/posts/ali-elixir-of-love/)

## Final Notes
### Keep The Global Footer Intact

You don’t have to override footer.html directly unless you want to style or modify it. PaperMod already includes the default footer showing that the site was built with Hugo and uses the PaperMod theme and I wanted to keep that intact. 

Initially, I went down this route (if not rabbit hole) of updating the footer.html direclty, only to discover that I accidently overrode the default footer `© 2025 Root & Reason · Powered by Hugo & PaperMod` with the affilaite content footer on all my pages. This is not what I desired and why I ended up overriding the content-footer for the affilaite link behavior that I desired. 

If you do override footer.html, make sure your custom footer.html includes the original less you override the original behavior entirely (unless thats desired):
```
<footer class="footer">
  <div class="container">
    <p>
      Built with <a href="https://gohugo.io/">Hugo</a> using <a href="https://github.com/adityatelange/hugo-PaperMod">PaperMod</a>.
    </p>
  </div>
</footer>
```

### Tips
* Do not put per-post images in the public/ directory. Put them in your post's folder under content/, and use Page Bundles so Hugo doesn’t rename or move your images unexpectedly.
* Always test with hugo server -D --cleanDestinationDir to preview your changes cleanly.
* Use version control (like Git) so you can track layout overrides and roll back changes.

## TL;DR
* Hugo allows layout overrides by matching file paths in layouts/
* You can selectively show custom footers without breaking global ones
* Frontmatter flags like `affiliate: true` help toggle features per-post
* Never edit theme files directly — always override them properly

