"""
# Sanitize data before sending it to the database to prevent SQL injection attacks


# All database transactions need to have a rollback in case of an error
# that way the database is not left in an inconsistent state
# This is done by using try/except blocks

@app.route('/buy_course')
@login_required
def buy_course():
    course_id = request.args.get('course_id')
    referrer = request.referrer

    # Validate course_id (assuming it's an integer)
    try:
        course_id = int(course_id)
    except (TypeError, ValueError):
        flash('Invalid course ID')
        return redirect(referrer)

    user_id = current_user.id

    # Check if the user already has the course
    has_course = UserCourses.query.filter_by(course_id=course_id, user_id=user_id).first()

    if not has_course:
        try:
            # Create a new UserCourses entry
            data_to_db = UserCourses(course_id=course_id, user_id=user_id)
            db.session.add(data_to_db)
            db.session.commit()
            flash('Course successfully purchased!')
        except Exception as e:
            db.session.rollback()
            flash('Failed to buy the course. Please try again later.')
            # Log the error for debugging purposes
            #print(f'Error: {e}')
    else:
        flash('You already own this course.')

    return redirect(referrer)





#in the add_course lets avoid a race condition ( if multiple users are accessing this code simultaneously) by checking if the course already exists
#before adding it to the database 
# Using a database auto-increment field for the image names can help avoid this issue as well

try:
    # Get the count of existing records in the Courses table
    existing_records_count = Courses.query.count()

    # Generate the image name based on the number of existing records
    data['image'] = f'image{existing_records_count + 1}'

    # Create a new Courses object with the provided data
    new_course = Courses(**data)

    # Add the new course data to the database
    db.session.add(new_course)
    db.session.commit()

    # Return a JSON response indicating success
    response = jsonify(Message="OK")
    response.headers.set('Access-Control-Allow-Origin', '*')
    print('Data successfully written')
    return response, 200

except Exception as e:
    # Handle database errors
    db.session.rollback()
    response = jsonify(Error=str(e))
    response.headers.set('Access-Control-Allow-Origin', '*')
    print('Failed to write data:', e)
    return response, 500


#def_home function the code is untidy and redundant
#instead lets declare the tite and subtitle variables outside the if/else block

@app.route('/', methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)
    courses = Courses.query.paginate(page, per_page=app.config['course_per_page'], error_out=False)
    
    title = "All Courses"
    subtitle = "Explore our unique courses"

    user_course_list = []
    if current_user.is_authenticated:
        user_courses_ids = UserCourses.query.filter_by(user_id=current_user.id).all()
        user_course_list = [course_id.course_id for course_id in user_courses_ids]

    return render_template('home.html', courses=courses, title=title, subtitle=subtitle, user_course_list=user_course_list)



"""
