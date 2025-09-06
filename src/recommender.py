import storage
import config
import embeddings


class CourseRecommender:
    def __init__(self):
        # load courses and past feedback
        self.courses = storage.load_json(config.COURSE_DATA_PATH, [])
        self.feedback = storage.load_json(config.FEEDBACK_DATA_PATH, {})

        # embeddings for all courses (yeah, might be slow first time)
        self.course_embeds = [embeddings.get_embedding(c["description"]) for c in self.courses]

    def recommend(self, user_profile, top_k=5, user_id="default"):
        # convert user profile to vector
        user_vec = embeddings.get_embedding(user_profile)

        scored = []
        for course, course_vec in zip(self.courses, self.course_embeds):
            score = embeddings.cosine_similarity(user_vec, course_vec)
            # give small boost if user liked these tags before
            score += self._tag_boost(user_id, course.get("tags", []))
            scored.append((score, course))

        # sort by score
        scored.sort(key=lambda x: x[0], reverse=True)

        # return just the courses
        return [c for _, c in scored[:top_k]]

    def _tag_boost(self, user_id, tags):
        # tiny boost for tags the user likes
        user_prefs = self.feedback.get(user_id, {}).get("tag_weights", {})
        return sum(user_prefs.get(t, 0) for t in tags) * 0.01

    def update_feedback(self, user_id, liked_tags=None, disliked_tags=None):
        if user_id not in self.feedback:
            self.feedback[user_id] = {"tag_weights": {}}

        tw = self.feedback[user_id]["tag_weights"]

        # add/subtract points for liked/disliked tags
        for t in liked_tags or []:
            tw[t] = tw.get(t, 0) + 1
        for t in disliked_tags or []:
            tw[t] = tw.get(t, 0) - 1

        storage.save_json(config.FEEDBACK_DATA_PATH, self.feedback)
