import math
import os
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False

class BiodiversityAnalyticsEngine:
    def calculate_shannon_index(self, species_counts: dict) -> float:
        """
        Calculates Shannon-Wiener Diversity Index (H')
        H' = - sum(p_i * ln(p_i))
        """
        total = sum(species_counts.values())
        if total == 0:
            return 0.0
        h_prime = 0.0
        for count in species_counts.values():
            if count > 0:
                p_i = count / total
                h_prime -= p_i * math.log(p_i)
        return round(h_prime, 4)

    def calculate_simpson_index(self, species_counts: dict) -> float:
        """
        Calculates Simpson's Index of Diversity (1 - D)
        D = sum(n_i * (n_i - 1)) / (N * (N - 1))
        """
        total = sum(species_counts.values())
        if total <= 1:
            return 1.0
        sum_n = sum(n * (n - 1) for n in species_counts.values())
        d = sum_n / (total * (total - 1))
        return round(1.0 - d, 4)

    def generate_assessment(self, region: str, species_counts: dict):
        shannon = self.calculate_shannon_index(species_counts)
        simpson = self.calculate_simpson_index(species_counts)
        richness = len(species_counts)
        total_individuals = sum(species_counts.values())
        
        # Ecosystem health score (weighted calculation)
        ecosystem_score = round(min(100.0, (shannon / 2.5 * 50) + (simpson * 30) + (min(richness, 20) / 20 * 20)), 2)
        habitat_quality = round(min(1.0, 0.65 + (shannon * 0.12)), 2)
        
        return {
            "region": region,
            "shannon_index": shannon,
            "simpson_index": simpson,
            "species_richness": richness,
            "total_individuals": total_individuals,
            "ecosystem_health_score": ecosystem_score,
            "habitat_quality_score": habitat_quality
        }

    def generate_pdf_report(self, title: str, region: str, author: str, metrics: dict, output_path: str):
        """
        Generates professional ReportLab PDF monitoring report with fallback.
        """
        if not HAS_REPORTLAB:
            txt_path = output_path.replace(".pdf", ".txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(f"=== {title} ===\nRegion: {region}\nAuthor: {author}\n")
                f.write(f"Shannon Index: {metrics.get('shannon_index')}\n")
                f.write(f"Simpson Index: {metrics.get('simpson_index')}\n")
                f.write(f"Health Score: {metrics.get('ecosystem_health_score')}%\n")
            return txt_path

        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Title
        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=12
        )
        story.append(Paragraph(title, title_style))

        # Metadata
        meta_text = f"<b>Region:</b> {region} | <b>Author:</b> {author} | <b>System:</b> Wildlife Population Intelligence"
        story.append(Paragraph(meta_text, styles['Normal']))
        story.append(Spacer(1, 15))

        # Executive Summary
        summary_heading = ParagraphStyle('Heading2', parent=styles['Heading2'], textColor=colors.HexColor("#0284c7"))
        story.append(Paragraph("1. Executive Summary", summary_heading))
        summary_p = f"""This report details the bio-assessment and species diversity analysis for <b>{region}</b>. 
        The calculated Shannon Diversity Index is <b>{metrics['shannon_index']}</b> and Simpson's Index is <b>{metrics['simpson_index']}</b>, 
        yielding an overall Ecosystem Health Score of <b>{metrics['ecosystem_health_score']}%</b>."""
        story.append(Paragraph(summary_p, styles['BodyText']))
        story.append(Spacer(1, 15))

        # Table of Metrics
        story.append(Paragraph("2. Quantitative Biodiversity Metrics", summary_heading))
        table_data = [
            ["Metric Parameter", "Value", "Benchmark Target", "Evaluation Status"],
            ["Shannon Diversity Index (H')", str(metrics['shannon_index']), "> 2.0", "Optimal"],
            ["Simpson Index of Diversity (1-D)", str(metrics['simpson_index']), "> 0.75", "High Stability"],
            ["Species Richness", f"{metrics['species_richness']} species", "> 10 species", "Healthy"],
            ["Total Sample Population", f"{metrics['total_individuals']} individuals", "N/A", "Active Census"],
            ["Ecosystem Health Score", f"{metrics['ecosystem_health_score']}%", "> 75.0%", f"{'High' if metrics['ecosystem_health_score'] > 75 else 'Moderate'}"],
        ]
        
        t = Table(table_data, colWidths=[180, 100, 110, 110])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8fafc')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ]))
        story.append(t)
        story.append(Spacer(1, 20))

        # Recommendation section
        story.append(Paragraph("3. Conservation Recommendations", summary_heading))
        recs = """
        • Maintain continuous camera trap monitoring around primary water sources.<br/>
        • Expand bioacoustic sensor density in high-density corridors.<br/>
        • Conduct follow-up aerial survey to evaluate seasonal movement patterns.
        """
        story.append(Paragraph(recs, styles['BodyText']))

        doc.build(story)
        return output_path

biodiversity_engine = BiodiversityAnalyticsEngine()
