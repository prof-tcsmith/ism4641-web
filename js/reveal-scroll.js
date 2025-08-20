// Reveal.js Scroll Enhancement JavaScript
// This script adds scroll indicators and improves scrolling behavior

document.addEventListener('DOMContentLoaded', function() {
    // Wait for Reveal.js to initialize
    if (typeof Reveal !== 'undefined') {
        Reveal.on('ready', function() {
            setupScrollableSlides();
        });
        
        Reveal.on('slidechanged', function() {
            setupScrollableSlides();
        });
    } else {
        // Fallback if Reveal isn't loaded yet
        setTimeout(function() {
            setupScrollableSlides();
        }, 1000);
    }
});

function setupScrollableSlides() {
    // Get all slides
    const slides = document.querySelectorAll('.reveal .slides section');
    
    slides.forEach(function(slide) {
        // Check if content overflows
        if (slide.scrollHeight > slide.clientHeight) {
            // Add class to indicate scrollable
            slide.classList.add('has-overflow');
            slide.classList.add('scrollable-slide');
            
            // Add scroll indicator if not already present
            if (!slide.querySelector('.scroll-indicator')) {
                const indicator = document.createElement('div');
                indicator.className = 'scroll-indicator';
                indicator.innerHTML = '↓ Scroll for more content ↓';
                indicator.style.cssText = `
                    position: fixed;
                    bottom: 70px;
                    left: 50%;
                    transform: translateX(-50%);
                    background: rgba(0, 103, 71, 0.9);
                    color: white;
                    padding: 8px 20px;
                    border-radius: 25px;
                    font-size: 14px;
                    z-index: 100;
                    pointer-events: none;
                    animation: pulse 2s infinite;
                    font-family: sans-serif;
                `;
                
                // Only show indicator on current slide
                if (slide.classList.contains('present')) {
                    document.body.appendChild(indicator);
                }
                
                // Hide indicator when user scrolls
                slide.addEventListener('scroll', function() {
                    if (slide.scrollTop > 50) {
                        if (indicator.parentNode) {
                            indicator.style.opacity = '0';
                            setTimeout(function() {
                                if (indicator.parentNode) {
                                    indicator.parentNode.removeChild(indicator);
                                }
                            }, 300);
                        }
                    }
                });
            }
        }
    });
    
    // Clean up indicators from non-present slides
    const currentSlide = document.querySelector('.reveal .slides section.present');
    if (currentSlide) {
        document.querySelectorAll('.scroll-indicator').forEach(function(indicator) {
            if (!currentSlide.contains(indicator) && indicator.parentNode === document.body) {
                indicator.parentNode.removeChild(indicator);
            }
        });
    }
}

// Add CSS animation if not already present
if (!document.querySelector('#scroll-indicator-styles')) {
    const style = document.createElement('style');
    style.id = 'scroll-indicator-styles';
    style.textContent = `
        @keyframes pulse {
            0%, 100% { 
                opacity: 0.7;
                transform: translateX(-50%) translateY(0);
            }
            50% { 
                opacity: 1;
                transform: translateX(-50%) translateY(-5px);
            }
        }
        
        .reveal .slides section {
            overflow-y: auto !important;
            overflow-x: hidden !important;
            height: 100vh !important;
            scrollbar-width: thin;
            scrollbar-color: rgba(0, 103, 71, 0.5) rgba(0, 0, 0, 0.1);
        }
        
        .reveal .slides section::-webkit-scrollbar {
            width: 12px;
        }
        
        .reveal .slides section::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        
        .reveal .slides section::-webkit-scrollbar-thumb {
            background: rgba(0, 103, 71, 0.5);
            border-radius: 10px;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .reveal .slides section::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 103, 71, 0.8);
        }
    `;
    document.head.appendChild(style);
}

// Handle keyboard navigation to ensure scrolling works
document.addEventListener('keydown', function(e) {
    const currentSlide = document.querySelector('.reveal .slides section.present');
    if (currentSlide && currentSlide.classList.contains('scrollable-slide')) {
        // Allow arrow keys to scroll within slide
        if (e.key === 'ArrowDown' || e.key === 'PageDown') {
            if (currentSlide.scrollTop + currentSlide.clientHeight < currentSlide.scrollHeight - 10) {
                e.preventDefault();
                currentSlide.scrollBy({
                    top: currentSlide.clientHeight * 0.8,
                    behavior: 'smooth'
                });
            }
        } else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
            if (currentSlide.scrollTop > 10) {
                e.preventDefault();
                currentSlide.scrollBy({
                    top: -currentSlide.clientHeight * 0.8,
                    behavior: 'smooth'
                });
            }
        }
    }
});

console.log('Reveal.js scroll enhancements loaded');