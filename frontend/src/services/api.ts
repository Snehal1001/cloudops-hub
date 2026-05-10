import axios from "axios";
import type { CreateProjectRequest } from "../types/project";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getProjects = async () => {
    const response = await api.get("/projects");
    return  response.data;
};

export const createProject = async (
  project: CreateProjectRequest
) => {
  const response = await api.post("/projects", project);
  console.log('create', response.data)
  return response.data;
};

export const deleteProject = async (projectId: number) => {
  const response = await api.delete(`/projects/${projectId}`);
  return response.data;
};

export default api;