import { useEffect, useState } from "react";

import {
  getProjects,
  createProject,
  deleteProject
} from "../services/api";

import type { Project } from "../types/project";

import ProjectForm from "../components/ProjectForm";
import ProjectList from "../components/ProjectList";

function Dashboard() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);

  const loadProjects = async () => {
    try {
      const data = await getProjects();
      setProjects(data);
    } catch (error) {
      console.error("Failed to load projects", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadProjects();
  }, []);

  const handleCreateProject = async (
    name: string,
    description: string
  ) => {
    try {
      const newProject = await createProject({
        name,
        description
      });

      setProjects((prev) => [...prev, newProject]);
    } catch (error) {
      console.error("Failed to create project", error);
    }
  };

  const handleDeleteProject = async (
    projectId: number
  ) => {
    try {
      await deleteProject(projectId);

      setProjects((prev) =>
        prev.filter((p) => p.id !== projectId)
      );
    } catch (error) {
      console.error("Failed to delete project", error);
    }
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>CloudOps Hub Dashboard</h1>

      <ProjectForm
        onCreate={handleCreateProject}
      />

      <hr />

      <ProjectList
        projects={projects}
        onDelete={handleDeleteProject}
      />
    </div>
  );
}

export default Dashboard;