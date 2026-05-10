import type { Project } from "../types/project";

interface Props {
  projects: Project[];
  onDelete: (projectId: number) => void;
}

function ProjectList({ projects, onDelete }: Props) {
  return (
    <div>
      <h2>Projects</h2>

      {projects.length === 0 ? (
        <p>No projects found.</p>
      ) : (
        <ul>
          {projects.map((project) => (
            <li
              key={project.id}
              style={{
                border: "1px solid #ccc",
                marginBottom: "10px",
                padding: "10px",
              }}
            >
              <h3>{project.name}</h3>

              <p>{project.description}</p>

              <button onClick={() => onDelete(project.id)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProjectList;