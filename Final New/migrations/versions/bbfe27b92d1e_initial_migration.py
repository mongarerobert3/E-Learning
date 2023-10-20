"""initial migration

Revision ID: bbfe27b92d1e
Revises: 
Create Date: 2023-10-20 15:20:58.849616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbfe27b92d1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('recommendation_score_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('recom_score_id1', sa.Float(), nullable=False),
    sa.Column('recom_score_id2', sa.Float(), nullable=False),
    sa.Column('recom_score_id3', sa.Float(), nullable=False),
    sa.Column('recom_score_id4', sa.Float(), nullable=False),
    sa.Column('recom_score_id5', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recommendation_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('recom_course_id1', sa.Integer(), nullable=False),
    sa.Column('recom_course_id2', sa.Integer(), nullable=False),
    sa.Column('recom_course_id3', sa.Integer(), nullable=False),
    sa.Column('recom_course_id4', sa.Integer(), nullable=False),
    sa.Column('recom_course_id5', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=False),
    sa.Column('subtitle', sa.String(length=500), nullable=True),
    sa.Column('page_url', sa.String(length=500), nullable=False),
    sa.Column('requirements', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('course_for', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('page_url'),
    sa.UniqueConstraint('title')
    )
    op.create_table('categories_table',
    sa.Column('categories_id', sa.Integer(), nullable=False),
    sa.Column('courses_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categories_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['courses_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('categories_id', 'courses_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories_table')
    op.drop_table('courses')
    op.drop_table('user_courses')
    op.drop_table('user')
    op.drop_table('recommendation_table')
    op.drop_table('recommendation_score_table')
    op.drop_table('categories')
    op.drop_table('author')
    # ### end Alembic commands ###
