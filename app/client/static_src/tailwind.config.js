/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    /**
     * Stylesheet generation mode.
     *
     * Set mode to "jit" if you want to generate your styles on-demand as you author your templates;
     * Set mode to "aot" if you want to generate the stylesheet in advance and purge later (aka legacy mode).
     */
    mode: "jit",

    purge: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /* 
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',
        
        /* 
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            maxHeight: {
                '864': '864px',
                '600': '600px',
                '75h': '75vh',
                '500': '500px',
            },
            height: {
                '80h': '80vh',
                '75h': '75vh',
                '70h': '70vh',
                '88': '88px',
                '500x': '500px',
                '600': '600px',
                '350x': '350px',
            },
            maxWidth: {
                '2/3': '66%',
            },
            minHeight: {
                '600': '600px',
                '550': '550px',
                '500': '500px',
                '65h': '65vh',
                '80h': '80vh',
                '60h': '60vh',
                '70h': '70vh',
                '75h': '75vh',   
            },
            borderRadius: {
                'large': '56px',
                '4xl': '64px',
            },
            boxShadow: {
                'ssl': '0px 4px 15px rgba(0, 0, 0, 0.25)',
            },
            dropShadow: {
                'ssl': '0px 4px 15px rgba(0, 0, 0, 0.25)',
                
            },
            marginLeft: {
                '1/3': '33%',
            },
            fontSize: {
                'h': ['20px', {
                    lineHeight: '23px',
                    fontWeight: '400',
                }],
            },
            colors: {
                'back': '#231D1C',
                'blue-back': '#2F364D',
                'tbrown': '#C0845E'
            },
        },
        

    },
    variants: {
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
