/* Save this as script.js */
(function() {
    const STORAGE_KEY = 'flotingBlog_posts';
    let posts = [];

    // --- DATA LOGIC ---
    function loadPosts() {
        const raw = localStorage.getItem(STORAGE_KEY);
        posts = raw ? JSON.parse(raw) : getSamplePosts();
        if (!raw) savePosts();
    }
    function savePosts() { localStorage.setItem(STORAGE_KEY, JSON.stringify(posts)); }
    
    function getSamplePosts() {
        return [{
            id: 'sample1', title: 'The Art of Slow Mornings', author: 'Luna Raye',
            category: 'Lifestyle', date: new Date().toISOString(),
            excerpt: 'Discover how embracing a slower morning...',
            content: 'Full content here...', imageUrl: 'https://picsum.photos/800/400?random=1'
        }];
    }

    // --- THEME LOGIC ---
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('flotingBlog_theme', next);
        });
    }

    // Apply stored theme on load
    const storedTheme = localStorage.getItem('flotingBlog_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', storedTheme);

    // Initialize
    loadPosts();
    
    // Export functions to global scope for the specific pages to use
    window.blogApp = { posts, savePosts, loadPosts, showToast: (msg, type) => console.log(msg) };
})();
