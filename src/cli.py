from recommender import CourseRecommender
from qa_agent import get_answer  # functional style


def main():
    print("********* Welcome to the Course Recommender CLI ************\n")
    user_name = input("Enter your name: ")
    background = input("Enter your background (e.g., 'Final-year CS student'): ")
    interests = input("Enter your interests (comma-separated): ")
    goals = input("Enter your career goals: ")

    if not background.strip() and not interests.strip() and not goals.strip():
        print("Profile is empty. Please enter some background, interests, or goals.")
        return []

    user_profile = f"Background: {background}\nInterests: {interests}\nGoals: {goals}"
    recommender = CourseRecommender()

    while True:
        print("\n--- Menu ---")
        print("1. Get course recommendations")
        print("2. Ask a career/learning question")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            top_courses = recommender.recommend(user_profile, top_k=5, user_id=user_name)
            print("\nTop 5 courses for you:")
            for idx, course in enumerate(top_courses, 1):
                tags = ", ".join(course.get("tags", []))
                print(f"{idx}. {course['title']} ({tags})")

            # feedback
            liked = input("\nWhich ones do you like? Numbers (comma) or skip: ")
            disliked = input("Which ones you dislike? Numbers (comma) or skip: ")

            liked_tags = []
            disliked_tags = []

            invalid_liked = []
            invalid_disliked = []

            for n in liked.split(","):
                n = n.strip()
                if n.isdigit():
                    idx = int(n) - 1
                    if 0 <= idx < len(top_courses):
                        liked_tags.extend(top_courses[idx].get("tags", []))
                    else:
                        invalid_liked.append(n)
                elif n:
                    invalid_liked.append(n)

            for n in disliked.split(","):
                n = n.strip()
                if n.isdigit():
                    idx = int(n) - 1
                    if 0 <= idx < len(top_courses):
                        disliked_tags.extend(top_courses[idx].get("tags", []))
                    else:
                        invalid_disliked.append(n)
                elif n:
                    invalid_disliked.append(n)

            if invalid_liked:
                print(f"\nSkipped invalid liked course numbers: {', '.join(invalid_liked)}")
            if invalid_disliked:
                print(f"Skipped invalid disliked course numbers: {', '.join(invalid_disliked)}")

            recommender.update_feedback(user_name, liked_tags, disliked_tags)
            print("\nFeedback recorded!!")

        elif choice == "2":
            question = input("Enter your question: ")
            answer = get_answer(question, user_profile=user_profile)
            print("\nAnswer:\n", answer)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("\nBad Input, please try again.")


if __name__ == "__main__":
    main()
