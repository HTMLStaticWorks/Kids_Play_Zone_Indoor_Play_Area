import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract top boilerplate (everything up to and including the mobile menu script)
mobile_menu_end = content.find('</script>', content.find('id="mobile-menu"')) + 9
top_part = content[:mobile_menu_end]

# Extract footer
footer_start = content.find('<!-- Footer -->')
bottom_part = content[footer_start:]

# New body content placeholder
new_body = """

<main class="w-full pt-[80px]">
    <!-- Split Hero Section -->
    <section class="relative px-margin-mobile md:px-margin-desktop py-12 md:py-24 max-w-container-max mx-auto overflow-hidden">
        <div class="grid md:grid-cols-2 gap-gutter items-center min-h-[600px]">
            <div class="z-10 relative flex flex-col items-start text-left mx-auto md:mx-0">
                <span class="bg-primary-fixed text-on-primary-fixed px-4 py-1 rounded-full font-label-md text-label-md mb-6 inline-block">The Ultimate Kids Experience</span>
                <h1 class="font-headline-xl text-headline-lg-mobile md:text-headline-xl text-primary mb-6 drop-shadow-sm">Where Imagination <br>Meets Adventure</h1>
                <p class="font-body-lg text-body-lg text-on-surface-variant dark:text-[#cbd5e1] mb-10 max-w-lg">
                    Discover a premium indoor play world designed for safety, fun, and endless smiles. Let your children explore, learn, and grow in a meticulously sanitized environment.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
                    <a href="package.html" class="bg-primary text-on-primary text-center px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform duration-150 shadow-md">Book a Party</a>
                    <a href="play zone.html" class="border-2 border-primary text-primary text-center px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform duration-150 shadow-md">Explore Zones</a>
                </div>
            </div>
            <div class="relative h-[400px] md:h-full w-full rounded-[40px] md:rounded-[60px] md:rounded-bl-[120px] overflow-hidden shadow-ambient order-first md:order-last mb-8 md:mb-0">
                <img class="w-full h-full object-cover object-center" data-alt="A vibrant, high-quality photograph of joyful children running and playing in a bright, modern indoor play center." src="https://lh3.googleusercontent.com/aida-public/AB6AXuD5xIw5h-mcL8QNnruaGME3w5l-yKj0E36a-2s1wXlW3r_l0hRjH936-aM0yQ5R0BfM74Bv_9vj9B66_8f7N7oWk-1y5H-8vO-4sO6h9p3g97gK8i15nF1g5a56J1Wf0w555W8e_9M1W1P298E7k4e9X6_2_150aQY6pT3N8Z-Gk1K2V_4Q01GZ1L"/>
                <!-- Decorative element -->
                <div class="absolute -bottom-10 -left-10 w-40 h-40 bg-secondary-container rounded-full blur-2xl opacity-50 z-0"></div>
            </div>
        </div>
        <!-- Decorative background elements -->
        <div class="absolute top-10 right-10 w-72 h-72 bg-primary-container opacity-20 rounded-full blur-3xl -z-10"></div>
    </section>

    <!-- Key Benefits Bar -->
    <section class="bg-surface-container-lowest dark:bg-[#122242] border-y border-outline-variant/20 shadow-sm py-12">
        <div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                <div class="flex items-center gap-4">
                    <div class="w-14 h-14 rounded-full bg-primary/10 flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-primary text-3xl">health_and_safety</span>
                    </div>
                    <div>
                        <h4 class="font-headline-md text-lg text-on-surface dark:text-[#f8fafc]">100% Safe</h4>
                        <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Fully padded facility</p>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <div class="w-14 h-14 rounded-full bg-secondary-container/30 flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-secondary text-3xl">coffee</span>
                    </div>
                    <div>
                        <h4 class="font-headline-md text-lg text-on-surface dark:text-[#f8fafc]">Parents Café</h4>
                        <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Relax while they play</p>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <div class="w-14 h-14 rounded-full bg-tertiary-container/30 flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-tertiary text-3xl">ac_unit</span>
                    </div>
                    <div>
                        <h4 class="font-headline-md text-lg text-on-surface dark:text-[#f8fafc]">Climate Controlled</h4>
                        <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Perfect temp year-round</p>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <div class="w-14 h-14 rounded-full bg-primary-fixed/50 flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-on-primary-fixed text-3xl">cleaning_services</span>
                    </div>
                    <div>
                        <h4 class="font-headline-md text-lg text-on-surface dark:text-[#f8fafc]">Deep Cleaned</h4>
                        <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Sanitized every night</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Interactive Zig-Zag Play Zones -->
    <section class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-24 flex flex-col gap-24">
        <div class="text-center">
            <h2 class="font-headline-lg text-headline-lg text-primary mb-4">Discover Our Zones</h2>
            <p class="font-body-md text-body-md text-on-surface-variant dark:text-[#cbd5e1] max-w-2xl mx-auto">From sensory exploration to thrilling obstacle courses, we have a world designed for every age.</p>
        </div>

        <!-- Zone 1: Toddler Town (Image Left) -->
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="h-[350px] md:h-[450px] rounded-[32px] overflow-hidden shadow-lg relative group">
                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 object-center" data-alt="Toddler play area" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD6bycy3sIqVT01ytdWQHf7q2gJbKL0LtFzpToHNL_4MX7-nHSWDfEYp8NTGNUpIcrZjwZvhjUcW_Ld6SfZW2uTJq95h4SHIBvgPWWdYmPjBO9izUv4X1A6Msf_SlQzjkdmvzNKSbGZFCAG6DZJHYReZlhvFpN4Rf44Gfxg380gDNA7gaZ6vjEKMOk_R2a4bIx4XUu58_t5GBT-_HDTVHgL7Eojt_SKVT-a4EYhtsuBuDI63td-6cVx"/>
                <div class="absolute inset-0 bg-primary/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <div class="flex flex-col items-start">
                <span class="bg-secondary-container text-on-secondary-container px-4 py-1 rounded-full font-label-md text-label-md mb-4">Ages 0-3</span>
                <h3 class="font-headline-xl text-4xl text-primary mb-4">Toddler Town</h3>
                <p class="font-body-lg text-body-lg text-on-surface-variant dark:text-[#cbd5e1] mb-6">A safe, soft, and gentle space filled with sensory panels, mini ball pits, and padded ramps perfectly sized for little explorers finding their feet.</p>
                <a href="play zone.html" class="font-label-md text-label-md text-primary flex items-center gap-2 hover:gap-3 transition-all">Explore Toddler Town <span class="material-symbols-outlined">arrow_forward</span></a>
            </div>
        </div>

        <!-- Zone 2: Junior Jungle (Image Right) -->
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="flex flex-col items-start order-2 md:order-1">
                <span class="bg-primary-fixed text-on-primary-fixed px-4 py-1 rounded-full font-label-md text-label-md mb-4">Ages 4-7</span>
                <h3 class="font-headline-xl text-4xl text-primary mb-4">Junior Jungle</h3>
                <p class="font-body-lg text-body-lg text-on-surface-variant dark:text-[#cbd5e1] mb-6">Watch them leap and swing through interactive floor games, role-play areas, and engaging physical challenges designed to spark creativity.</p>
                <a href="play zone.html" class="font-label-md text-label-md text-primary flex items-center gap-2 hover:gap-3 transition-all">Explore Junior Jungle <span class="material-symbols-outlined">arrow_forward</span></a>
            </div>
            <div class="h-[350px] md:h-[450px] rounded-[32px] overflow-hidden shadow-lg relative group order-1 md:order-2">
                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 object-center" data-alt="Junior play area" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAsozR-VlY4fDetVze1il5MMBR20dsgcxyB23DYPdgURHvUoKm73TCxA3NeL5rmQ3nD6fgpq4yvFyEfBPjZx3hC1drEcNQHN9CpoVmtLysIAaEVJWaZEQS72ddW6YBgqBfx9rvH6bSQ7n2x3U6k_Irn93OgjwynA1hBwd3TmIch8knibAwG5kJ8oUglGL-VEIPLNkPf3OkCS4KuXASvXiFP0dosvqUAO_T8ZlH5jB7Uv326OyGoCBVp"/>
                <div class="absolute inset-0 bg-primary/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
        </div>

        <!-- Zone 3: Adventure Arena (Image Left) -->
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="h-[350px] md:h-[450px] rounded-[32px] overflow-hidden shadow-lg relative group">
                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 object-center" data-alt="Adventure play area" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAF6LempW4YwPCNmdPTQbHQymRZC9mEn9OWs4CuoDG5ufexJVHk0zbWW_HFhH4sMBDEU47rBZJb_7RQjvVdxLuh4jK1XfOpp-Bk2d-9Ns2XGwhJWkZPhP_G2y31WFoflZbiU-stq2d0Twq00pt46eWBj_QOoqEGZdvjVoxCl-2HcaPZbVJIVl67-C_c_9A4xaXI98W0MZzTe8AP_rlmjj9bEXU69cCADvfiWDVLaeKGaWpeEDpYzrAf"/>
                <div class="absolute inset-0 bg-primary/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <div class="flex flex-col items-start">
                <span class="bg-tertiary-container text-on-tertiary-container px-4 py-1 rounded-full font-label-md text-label-md mb-4">Ages 8-12</span>
                <h3 class="font-headline-xl text-4xl text-primary mb-4">Adventure Arena</h3>
                <p class="font-body-lg text-body-lg text-on-surface-variant dark:text-[#cbd5e1] mb-6">A thrilling, high-energy zone featuring multi-level climbing frames, rope bridges, and mega slides for older kids seeking an ultimate physical challenge.</p>
                <a href="play zone.html" class="font-label-md text-label-md text-primary flex items-center gap-2 hover:gap-3 transition-all">Explore Adventure Arena <span class="material-symbols-outlined">arrow_forward</span></a>
            </div>
        </div>
    </section>

    <!-- Parent Testimonials Section -->
    <section class="bg-surface-container-low dark:bg-[#1a2a4a] py-24">
        <div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
            <div class="text-center mb-16">
                <h2 class="font-headline-lg text-headline-lg text-primary mb-4">Loved by Parents &amp; Kids Alike</h2>
                <p class="font-body-md text-body-md text-on-surface-variant dark:text-[#cbd5e1] max-w-2xl mx-auto">Don't just take our word for it. Here is what our community has to say about PlayZone.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Testimonial 1 -->
                <div class="bg-surface-container-lowest dark:bg-[#122242] p-8 rounded-[24px] shadow-sm relative">
                    <span class="material-symbols-outlined text-primary/20 text-6xl absolute top-4 right-4">format_quote</span>
                    <div class="flex text-secondary mb-4">
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    </div>
                    <p class="font-body-lg italic text-on-surface dark:text-[#f8fafc] mb-6 relative z-10">"Absolutely the cleanest and most well-maintained indoor playground we have ever visited. My kids loved the giant ball pit!"</p>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center font-bold text-primary">SM</div>
                        <div>
                            <h4 class="font-label-md text-on-surface dark:text-[#f8fafc]">Sarah Mitchell</h4>
                            <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Mother of 2</p>
                        </div>
                    </div>
                </div>
                <!-- Testimonial 2 -->
                <div class="bg-surface-container-lowest dark:bg-[#122242] p-8 rounded-[24px] shadow-sm relative md:-translate-y-4">
                    <span class="material-symbols-outlined text-primary/20 text-6xl absolute top-4 right-4">format_quote</span>
                    <div class="flex text-secondary mb-4">
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    </div>
                    <p class="font-body-lg italic text-on-surface dark:text-[#f8fafc] mb-6 relative z-10">"We hosted my son's 5th birthday party here. The staff took care of EVERYTHING. It was stress-free and magical. Highly recommend the VIP package!"</p>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-secondary/10 rounded-full flex items-center justify-center font-bold text-secondary">DJ</div>
                        <div>
                            <h4 class="font-label-md text-on-surface dark:text-[#f8fafc]">David Johnson</h4>
                            <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Local Guide</p>
                        </div>
                    </div>
                </div>
                <!-- Testimonial 3 -->
                <div class="bg-surface-container-lowest dark:bg-[#122242] p-8 rounded-[24px] shadow-sm relative">
                    <span class="material-symbols-outlined text-primary/20 text-6xl absolute top-4 right-4">format_quote</span>
                    <div class="flex text-secondary mb-4">
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    </div>
                    <p class="font-body-lg italic text-on-surface dark:text-[#f8fafc] mb-6 relative z-10">"The parents' cafe is a lifesaver. Great wifi, amazing coffee, and I can easily see my toddler playing safely from my table."</p>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-tertiary/10 rounded-full flex items-center justify-center font-bold text-tertiary">ET</div>
                        <div>
                            <h4 class="font-label-md text-on-surface dark:text-[#f8fafc]">Emily Tran</h4>
                            <p class="font-body-md text-sm text-on-surface-variant dark:text-[#cbd5e1]">Freelancer</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Quick Pricing / Membership Snapshot -->
    <section class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-24">
        <div class="bg-primary rounded-[40px] overflow-hidden shadow-ambient relative">
            <div class="absolute inset-0 bg-[url('https://lh3.googleusercontent.com/aida-public/AB6AXuA2ydApm2cm0WJuTJyQNI8EqAd0Fr1rGfzqi7I9UYZmGa-JIOiBspvLlrOfioempc2N_3rqOXZNkLV5WN52HpVJm_Hxh_Ml2u7jSKMBD3-Wekxb0wekLqUYSoi3UFKLnrLalC5h7PSYBPz2Hq1zBFMny2_FgbmnRw3c2qLy9wk-hTEgJHiNTQl_ufQbxG8Jr9FBSep2jxfA54nN-dc_pTIUejWZvwKHxfhPxrv0S-IkNhb0DGszJPYl')] bg-cover bg-center opacity-10 mix-blend-overlay"></div>
            <div class="grid md:grid-cols-2 p-10 md:p-16 gap-12 relative z-10 items-center">
                <div class="text-on-primary">
                    <h2 class="font-headline-xl text-4xl mb-4">Unlimited Play All Month Long</h2>
                    <p class="font-body-lg mb-8 opacity-90">Become a PlayZone Member today and enjoy unrestricted access, exclusive discounts on cafe food, and priority booking for events.</p>
                    <div class="flex items-center gap-4">
                        <span class="text-5xl font-extrabold">$49</span>
                        <span class="font-body-md opacity-80">/ month<br>per child</span>
                    </div>
                </div>
                <div class="flex flex-col sm:flex-row gap-4 justify-end">
                    <a href="package.html" class="bg-surface/20 hover:bg-surface/30 backdrop-blur-md border border-surface/50 text-on-primary px-8 py-4 rounded-full font-label-md text-label-md transition-all text-center">View Day Passes</a>
                    <a href="membership.html" class="bg-secondary text-on-secondary px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform shadow-md text-center">Get Membership</a>
                </div>
            </div>
        </div>
    </section>

</main>

"""

# Combine parts
full_content = top_part + new_body + bottom_part

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(full_content)
    
print("Created home2.html")
