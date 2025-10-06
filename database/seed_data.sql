-- Sample data for testing and development
-- Run this after creating the schema to populate with sample records

-- Insert sample projects
INSERT INTO projects (project_name, description, start_date, status) VALUES
('Website Redesign', 'Complete overhaul of company website with modern UI/UX', '2024-01-15', 'In Progress'),
('Mobile App Development', 'Native mobile app for iOS and Android platforms', '2024-02-01', 'In Progress'),
('Database Migration', 'Migrate legacy database to cloud infrastructure', '2024-03-10', 'Planning'),
('Marketing Campaign', 'Q2 digital marketing campaign across social media', '2024-04-01', 'Not Started'),
('Security Audit', 'Comprehensive security review and penetration testing', '2024-02-15', 'In Progress'),
('Customer Portal', 'Self-service portal for customer account management', '2024-05-01', 'Not Started');

-- Insert sample tasks
INSERT INTO tasks (task_name, project_id, description, due_date, priority, status) VALUES
('Design Homepage Mockup', 1, 'Create initial homepage design concepts', '2024-02-01', 'High', 'Completed'),
('Implement Navigation', 1, 'Build responsive navigation menu', '2024-02-15', 'High', 'In Progress'),
('Setup Testing Environment', 1, 'Configure staging server for testing', '2024-02-20', 'Medium', 'Not Started'),
('iOS App Framework', 2, 'Setup initial iOS project structure', '2024-02-10', 'High', 'In Progress'),
('Android App Framework', 2, 'Setup initial Android project structure', '2024-02-10', 'High', 'In Progress'),
('User Authentication', 2, 'Implement login and registration', '2024-03-01', 'High', 'Not Started'),
('Database Schema Design', 3, 'Design new database schema', '2024-03-15', 'High', 'In Progress'),
('Data Migration Script', 3, 'Write scripts to migrate existing data', '2024-04-01', 'High', 'Not Started'),
('Social Media Strategy', 4, 'Develop content calendar and strategy', '2024-04-10', 'Medium', 'Not Started'),
('Create Ad Campaigns', 4, 'Design and launch paid advertising', '2024-04-15', 'Medium', 'Not Started'),
('Vulnerability Assessment', 5, 'Conduct initial vulnerability scan', '2024-02-20', 'High', 'In Progress'),
('Penetration Testing', 5, 'Perform controlled penetration tests', '2024-03-05', 'High', 'Not Started'),
('Portal Design', 6, 'Design customer portal interface', '2024-05-10', 'Medium', 'Not Started'),
('Account Management Features', 6, 'Build account management functionality', '2024-05-20', 'Medium', 'Not Started');
