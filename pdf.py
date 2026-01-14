from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Base fonts
pdf.set_font("Arial", size=12)

# Header
pdf.set_font("Arial", "B", 18)
pdf.cell(0, 10, "TUFAIL ABBAS", ln=True, align="C")
pdf.set_font("Arial", size=12)
pdf.cell(0, 7, "MERN Stack Developer | Frontend Specialist", ln=True, align="C")
pdf.ln(5)

# Contact details
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, "📍 Skardu, Gilgit Baltistan, Pakistan | 📧 tufail206abbas@gmail.com")
pdf.multi_cell(0, 5, "📞 0342-5514198 | WhatsApp: 0355-5040206")
pdf.multi_cell(0, 5, "🌐 GitHub: github.com/tufail206 | LinkedIn: linkedin.com/in/tufail-abbas-bb9b83299")
pdf.ln(5)

# Sections
def add_section(title):
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 6, title, ln=True)
    pdf.set_font("Arial", size=10)

add_section("PROFESSIONAL SUMMARY")
pdf.multi_cell(0, 5, "Frontend-focused MERN Stack Developer with 2+ years of frontend experience and 1+ year of backend experience. Skilled in building modern, responsive, and performance-optimized web applications. Expertise in React.js, Next.js, TypeScript, Tailwind CSS, and modern UI libraries. Experienced in API integration, authentication systems, state management, and scalable frontend architectures. Passionate about clean code, UI performance, and collaborative development.")
pdf.ln(3)

add_section("TECHNICAL SKILLS")
skills = """
Frontend & Libraries: JavaScript (ES6+), React.js, Redux Toolkit & RTK Query, Next.js, TypeScript, HTML5, CSS3, Responsive Design
UI & Styling: Tailwind CSS, Bootstrap, Material UI, ShadCN UI, DaisyUI, Framer Motion
Backend & Database: Node.js, Express.js, REST APIs, MongoDB, Prisma ORM, PostgreSQL, MySQL, JWT, Socket.IO
Tools & Others: Git & GitHub, Postman, Figma
"""
pdf.multi_cell(0, 5, skills.strip())
pdf.ln(3)

add_section("PROFESSIONAL EXPERIENCE")
pdf.multi_cell(0, 5, "MERN Stack Developer — Digital Pine (Sep 2024 – Oct 2025)\n• Built modern, responsive web applications for 3+ client projects, improving user engagement by 30%\n• Developed 10+ reusable frontend components\n• Integrated REST APIs and secure JWT authentication\n• Customized UI libraries to match branding")
pdf.ln(2)
pdf.multi_cell(0, 5, "MERN Stack Developer Intern — Digital Pine (Mar 2024 – Aug 2024)\n• Assisted in MERN projects, focusing on frontend\n• Built responsive React components\n• Implemented authentication and API integration")
pdf.ln(2)
pdf.multi_cell(0, 5, "Frontend Instructor — Next Planner Academy (Jun 2024 – Sep 2024)\n• Taught HTML, CSS, JavaScript, React\n• Guided students on real‑world frontend workflows")
pdf.ln(3)

add_section("PROJECTS")
pdf.multi_cell(0, 5, "Karakurum Magic — Frontend (Next.js, TypeScript, Tailwind CSS)\nAlpine Adventure Guide — Frontend (Next.js, TypeScript, Tailwind CSS)\nMERN E‑Commerce — React, Node, MongoDB, Stripe")
pdf.ln(3)

add_section("EDUCATION")
pdf.multi_cell(0, 5, "BSc Computer Science, Baltistan University, Skardu (2023–2026)\nIntermediate, Govt. Boys Degree College, Skardu (2021–2022)\nMatriculation, USWA Public School, Skardu (2019–2020)")
pdf.ln(3)

add_section("CERTIFICATIONS")
pdf.multi_cell(0, 5, "MERN Stack Developer Certificate — Digital Pine (Mar 2024 – Aug 2025)\nProfessional Certification — NAVTTAC")
pdf.ln(3)

add_section("LANGUAGES")
pdf.multi_cell(0, 5, "English (Professional)\nUrdu (Native)")
pdf.ln(3)

add_section("STRENGTHS")
pdf.multi_cell(0, 5, "Strong frontend architecture and UI skills\nClean, maintainable code\nProblem‑solving and debugging\nPerformance‑focused mindset\nCollaborative work style")

# Save PDF
pdf.output("Tufail_Abbas_Resume.pdf")
print("PDF created successfully!")
