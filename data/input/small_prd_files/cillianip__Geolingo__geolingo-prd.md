---
project: Geolingo
repository: cillianip/Geolingo
license: MIT License
source_file: geolingo-prd.md
source_url: https://github.com/cillianip/Geolingo/blob/54c55c51d38f150710d06aec937cdd0fc7ecc278/geolingo-prd.md
downloaded_at: 2025-12-05T10:45:16.039195+00:00
consensus_grade_level: 16.2
headings_per_sentence: 0.51
lists_per_sentence: 2.24
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.29
anaphora_per_sentence: 0.14
sentence_cv: 1.003
cpre_terms_per_sentence: 1.0
---
# GeoLingo: Language Guessing Game
## Product Requirements Document

### 1. Product Overview
GeoLingo is an educational web-based game that challenges players to identify the geographic origin of languages by listening to the phrase "I don't know" spoken in different languages. Players select countries on an interactive world map, earning points for correct guesses while learning about global linguistic diversity.

### 2. Target Audience
- Language enthusiasts and polyglots
- Students (high school and university level)
- Geography hobbyists
- Casual gamers interested in educational content
- Language teachers and educators looking for interactive classroom tools

### 3. Product Objectives
- Create an engaging, educational game that improves geographic and linguistic awareness
- Showcase the diversity of global languages in an interactive format
- Provide a smooth, intuitive user experience that works across devices
- Support at least 40 languages in the initial release
- Implement a scoring system that encourages repeated play

### 4. Success Metrics
- User engagement: Average session duration of 5+ minutes
- Learning outcomes: 80% of users report increased knowledge of global languages
- Retention: 30% of users return for a second session
- Social sharing: 10% of users share their results on social media
- Geographic reach: Users from at least 20 different countries

### 5. User Journey

#### 5.1 Core Game Loop
1. Player starts the game and is presented with the main interface
2. Audio automatically plays: "I don't know" in a randomly selected language
3. Player can replay the audio as many times as needed
4. Player hovers over countries on the map to see country names
5. Player clicks on the country they believe is the source of the language
6. Feedback is provided (correct/incorrect)
7. If correct:
   - Points are awarded based on difficulty and speed
   - Information about the language is displayed
8. If incorrect:
   - The correct answer is shown with the distance from the player's guess
   - Reduced points may be awarded for close guesses (neighboring countries)
9. Next round begins with a new language

#### 5.2 Game Modes
- **Standard Mode**: Random selection of languages from the full database
- **Regional Mode**: Focus on languages from a specific continent or region
- **Challenge Mode**: Timed rounds with increasing difficulty
- **Language Family Mode**: Focus on related language groups

### 6. Functional Requirements

#### 6.1 Audio System
- Generate or play "I don't know" in 40+ languages
- Include replay button for listening multiple times
- Audio must be clear and authentic to each language
- Support for volume control
- Fallback mechanism if TTS is unavailable

#### 6.2 Map Interface
- Interactive world map showing country boundaries
- Hover state that highlights countries and displays their names
- Click/tap functionality for country selection
- Visual indication of previous guesses
- Zoom and pan capabilities for mobile users
- Optional region/continent filter

#### 6.3 Game Mechanics
- Scoring system based on:
  - Accuracy (exact country or neighboring country)
  - Speed of response (timer for each round)
  - Streak of correct answers
  - Difficulty of the language (categorized as common, uncommon, rare)
- Progress tracking across sessions (if user opts in)
- Leaderboard for competitive players
- Achievement system (e.g., "Polyglot" for 10 correct guesses)

#### 6.4 Educational Content
- Brief information about each language after correct guess
  - Name of the language
  - Number of speakers worldwide
  - Interesting facts about the language
  - Countries where it's spoken (primary and secondary)
  - Language family information
- Optional "Learn More" resources

#### 6.5 User Accounts (Optional for MVP)
- Anonymous play with session storage
- Optional account creation for:
  - Saving progress
  - Tracking statistics
  - Competing on leaderboards
  - Customizing preferences

### 7. Technical Requirements

#### 7.1 Frontend Stack
- React framework for component-based UI
- Responsive design for desktop and mobile
- State management using React Context or Redux
- Tailwind CSS for styling
- Vite for fast builds and development

#### 7.2 Map Implementation
- SVG-based world map using react-simple-maps
- Country data from Natural Earth or similar open-source map data
- Hover and selection states for all countries
- Responsive scaling for different screen sizes

#### 7.3 Audio System
- Primary: Web Speech API for text-to-speech
- Backup: Pre-recorded audio files for languages not supported by Web Speech API
- Audio player controls via Howler.js
- Audio caching to reduce load times for repeat plays

#### 7.4 Data Requirements
- JSON database of languages including:
  - Text phrase "I don't know" in each language
  - Primary countries where the language is spoken
  - Secondary countries where it's also common
  - Language difficulty rating
  - Language family information
  - Brief educational content
- Country data including:
  - ISO codes
  - Geographical coordinates
  - Neighbor countries (for partial scoring)
  - Continental/regional grouping

#### 7.5 Persistence
- LocalStorage for game history and user preferences
- Optional backend for user accounts and leaderboards (Phase 2)

#### 7.6 Analytics
- Basic game analytics (rounds played, languages guessed, etc.)
- Heatmap of guesses to identify difficult languages
- Session duration and engagement metrics

### 8. User Interface Design

#### 8.1 Main Game Screen
- Top section: Game header, score, current round counter
- Center: Interactive world map (largest component)
- Bottom: Audio controls, hint button, skip button
- Right sidebar: Game information, settings, leaderboard access

#### 8.2 Results Modal
- Appears after each guess
- Shows correct answer on map
- Displays language information
- Shows points earned
- Contains "Next Round" button

#### 8.3 Game Over Screen
- Final score
- Performance summary (accuracy percentage, best language family)
- Shareable results card
- Play again button
- Option to view global leaderboard

#### 8.4 Settings Panel
- Volume control
- Difficulty settings
- Regional focus options
- Dark/light mode toggle
- Language selection for UI (not game content)

### 9. Accessibility Requirements
- Keyboard navigation for map selection
- Color blindness considerations for map highlighting
- Alternative text-based mode for visually impaired users
- Closed captions or visual cues as alternatives to audio
- Support for screen readers
- Compliance with WCAG 2.1 AA standards

### 10. Performance Requirements
- Initial load time under 3 seconds on broadband
- Audio playback delay under 500ms
- Smooth map interactions (60fps for animations)
- Support for latest 2 versions of major browsers
- Responsive design for screens from 320px to 4K
- Offline capabilities for core gameplay

### 11. Deployment Strategy
- Initial beta release with 20 languages
- Full release with 40+ languages
- Continuous deployment pipeline via GitHub Actions
- Hosting on Netlify/Vercel for global CDN
- Analytics integration for usage monitoring

### 12. Future Enhancements (Post-MVP)
- Expanded language database (goal: 100+ languages)
- Multiplayer mode for classroom or friend competition
- Language learning extensions (basic phrases beyond "I don't know")
- Custom game creation for teachers
- Mobile app version for iOS and Android
- Integration with language learning platforms

### 13. Timeline and Milestones
1. **Week 1-2**: Technical prototype with map and basic audio
2. **Week 3-4**: Core gameplay implementation with 10 test languages
3. **Week 5-6**: UI refinement and addition of educational content
4. **Week 7-8**: Expansion to 40 languages and testing
5. **Week 9**: Beta release and feedback collection
6. **Week 10-11**: Refinements based on beta feedback
7. **Week 12**: Full public release

### 14. Technical Risks and Mitigation
- **Risk**: Web Speech API language support varies by browser
  - **Mitigation**: Pre-recorded audio fallbacks for all languages
- **Risk**: Map interaction performance on mobile devices
  - **Mitigation**: Optimized SVG map with reduced detail on mobile
- **Risk**: Data size for many languages affecting load time
  - **Mitigation**: Progressive loading and caching strategies

### 15. Success Evaluation
After three months of release, the product will be evaluated based on:
- User acquisition and retention metrics
- Gameplay statistics (completion rates, accuracy, preferred languages)
- User feedback and satisfaction scores
- Performance against initial success metrics
- Technical stability and bug reports

### 16. Appendix

#### 16.1 Sample Language Data (Initial 10 Languages)
```json
{
  "french": {
    "phrase": "Je ne sais pas",
    "phoneticSpelling": "zhuh nuh say pah",
    "countries": ["France", "Belgium", "Switzerland", "Canada", "Monaco"],
    "primaryCountry": "France",
    "speakers": "275 million",
    "difficulty": "common",
    "languageFamily": "Romance",
    "funFact": "French was the official language of England for over 300 years"
  },
  "japanese": {
    "phrase": "分かりません",
    "phoneticSpelling": "wa-ka-ri-ma-sen",
    "countries": ["Japan"],
    "primaryCountry": "Japan",
    "speakers": "125 million",
    "difficulty": "common",
    "languageFamily": "Japonic",
    "funFact": "Japanese has three different writing systems used simultaneously"
  }
}
```

#### 16.2 Technical Dependencies
- React 18+
- react-simple-maps
- Web Speech API
- Howler.js
- i18n-iso-countries
- Tailwind CSS
- Vite
