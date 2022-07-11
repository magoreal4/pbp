module.exports = {
    important: true,
    darkMode: 'class',
    content: [
        // Templates within theme app (e.g. base.html)
        // '../templates/**/*.html',
        // Templates in other apps
        '../../templates/**/*.html',
        // Ignore files in node_modules 
        '!../../**/node_modules',
        // Include JavaScript files that might contain Tailwind CSS classes      
        // '../../**/*.js',
        // Include Python files that might contain Tailwind CSS classes
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                "primary": "#ee7e25",
                "primary-light": "#ffb057",
                'secondary-light': '#bac5b9',
                'secondary': '#032900',
                'secondary-dark': '#051900',
                "neutral": "#23282F",
                "info": "#90cbd4",
                "success": "#6CB288",
                "warning": "#fdcb10",
                "error": "#fc483f",
                'facebook': '#3b5998',
                'whatsapp': '#25d366'
            },
            height: {
                'screen75': '75vh',
                'screen80': '80vh',
            },
            dropShadow: {
                'black': '0px 0px 6px black',
            },
            fontFamily: {
                'specialElite': ['Special Elite', 'cursive'],
                'SecularOne': ['Secular One', 'sans-serif']
              },
            animation: {
                "text-flicker-in-glow": "text-flicker-in-glow 3s linear both",
                "fade-in-fwd": "fade-in-fwd 4s cubic-bezier(0.390, 0.575, 0.565, 1.000) both",
            },
            keyframes: {
                "text-flicker-in-glow": {
                    "0%": {
                        opacity: "0"
                    },
                    "10%,10.2%,20%,20.6%,30%,30.6%,45%,55.1%,57%,60.1%,65%,75.1%,77%,85.1%,86%": {
                        opacity: "0",
                        "text-shadow": "none"
                    },
                    "10.1%": {
                        opacity: "1",
                        "text-shadow": "none"
                    },
                    "20.1%": {
                        opacity: "1",
                        "text-shadow": "0 0 30px rgba(255, 255, 255, .25)"
                    },
                    "30.1%,30.5%,45.1%,50%,55%": {
                        opacity: "1",
                        "text-shadow": "0 0 30px rgba(255, 255, 255, .45), 0 0 60px rgba(255, 255, 255, .25)"
                    },
                    "57.1%,60%": {
                        opacity: "1",
                        "text-shadow": "0 0 30px rgba(255, 255, 255, .55), 0 0 60px rgba(255, 255, 255, .35)"
                    },
                    "65.1%,75%": {
                        opacity: "1",
                        "text-shadow": "0 0 30px rgba(255, 255, 255, .55), 0 0 60px rgba(255, 255, 255, .35), 0 0 100px rgba(255, 255, 255, .1)"
                    },
                    "77.1%,85%": {
                        opacity: "1",
                        "text-shadow": "0 0 30px rgba(255, 255, 255, .55), 0 0 60px rgba(255, 255, 255, .4), 0 0 110px rgba(255, 255, 255, .2), 0 0 100px rgba(255, 255, 255, .1)"
                    },
                    "86.1%,to": {
                        opacity: "1",
                        "text-shadow": "0 0 30px rgba(255, 255, 255, .6), 0 0 60px rgba(255, 255, 255, .45), 0 0 110px rgba(255, 255, 255, .25), 0 0 100px rgba(255, 255, 255, .1)"
                    }
                },
                "fade-in-fwd": {
                    "0%": {                        
                        opacity: "0"
                    },
                    to: {                        
                        opacity: "1"
                    }
                },
            },
        },
    },
    plugins: [
        // require('@tailwindcss/aspect-ratio'),
        // require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        // require('@tailwindcss/line-clamp'),
        
    ],
}