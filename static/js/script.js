document.addEventListener("DOMContentLoaded", () => {
	// --- Parallax: translate banner images inside fixed-height containers on desktop ---
		// ...existing code...
	
	(function () {
		const BREAKPOINT = 768; // desktop when parallax active
		const MOTION_INTENSITY = 0.55; // 0-1, lower = subtler movement (reduce to show more of image)
		const containers = Array.from(document.querySelectorAll('.parallax-container'));
		if (!containers.length) return;
	
		let ticking = false;
	
		function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
	
		function updateOne(container) {
			if (window.innerWidth < BREAKPOINT) return; // disabled on mobile
	
			const img = container.querySelector('.parallax-item');
			if (!img) return;
	
			const crect = container.getBoundingClientRect();
			const viewportCenter = window.innerHeight / 2;
			const elementCenter = crect.top + crect.height / 2;
	
			// normalized distance [-1,1] (container center relative to viewport center)
			const denom = (window.innerHeight / 2) + (crect.height / 2);
			let relative = (viewportCenter - elementCenter) / denom;
			relative = clamp(relative, -1, 1);
	
			const imgRect = img.getBoundingClientRect();
			const imgHeight = imgRect.height;
			const containerHeight = crect.height;
			const maxTranslate = Math.max(0, (imgHeight - containerHeight) / 2);
	
			// reduce amplitude with MOTION_INTENSITY so the effect is more slight
			const translate = relative * maxTranslate * MOTION_INTENSITY; // px
	
			// preserve horizontal centering (translateX(-50%)) and shift vertically
			img.style.transform = `translate(-50%, calc(-50% + ${translate}px))`;
		}
	
		function updateAll() {
			containers.forEach(updateOne);
			ticking = false;
		}
	
		function onScrollOrResize() {
			if (!ticking) {
				window.requestAnimationFrame(updateAll);
				ticking = true;
			}
		}
	
		// run after images load (some images may already be loaded)
		window.addEventListener('load', onScrollOrResize, { passive: true });
		window.addEventListener('resize', onScrollOrResize, { passive: true });
		window.addEventListener('scroll', onScrollOrResize, { passive: true });
	
		// initial run
		onScrollOrResize();
	})();
	
});
